import sys
import numpy as np

import parmed
from parmed import unit as u

import tex_sampling.pyrex as pyrex

def main():
    thing = generate_rwmd_temperatures(heating_duration=1000*u.picoseconds,
                                    cooling_rate=10*u.picosecond/u.kelvin)

def generate_rwmd_temperatures(current_T=305*u.kelvin, timestep=2.0*u.femtoseconds,
                                dT=10*u.kelvin, 
                                heating_duration=30000*u.picoseconds,
                                interval_duration=5*u.picoseconds,
                                t_pairs=np.asarray([305,455]) * u.kelvin,
                                cooling_rate=1000*u.picosecond/u.kelvin):
    """ Generate an array of RWMD temperatures 

    Parameters
    ----------
    current_T : parmed.Unit, u.kelvin
    timestep : parmed.Unit, u.femtosconds
    dT : parmed.Unit, u.kelvin
        Temperature window spacing
    heating_duration : parmed.Unit, u.picoseconds
        Duration of full heating phase
    interval_duration : parmed.Unit, u.picoseconds
        Duration between temperature moves
    t_pairs : parmed.Unit, u.kelvin
        Temperature range 
    cooling_rate : parmed.unit, u.picosecond/u.kelvin
        Every cooling_rate picoseconds, drop the RWMD ceiling by 1 K

    Returns
    -------
    all_temps : np.ndarray

    Notes
    -----
    This script doesn't account for multiple thermostating groups. Currently, I'm
    not sure how to best implement multiple thermostatting groups.
    """
    _validate_units(**locals())

    # The full heating phase
    heating_steps = int((heating_duration / timestep)) # steps
    interval_steps = int((interval_duration / timestep))  #steps

    sim_time = 0*u.picoseconds

    cooling_rate_steps = cooling_rate * dT / timestep
    total_cooling_time = (t_pairs[1] - t_pairs[0]) * cooling_rate
    total_cooling_steps = int(total_cooling_time / timestep)


    for step in range(0, heating_steps):
            sim_time += timestep
            # Initialization
            if step == 0:
                freq = pyrex.init_freq_dict(t_pairs[0]._value, t_pairs[1]._value, 
                                            dT._value, T_init=current_T._value)
                heating_temps = np.zeros(int(heating_steps/interval_steps) ) *u.kelvin
                heating_temps[0] = current_T
                
            # Attempt to change temperature
            if step % interval_steps == 0:
                current_T = pyrex.choose_next_T(freq, current_T._value, 
                                                dT._value) * u.kelvin
                heating_temps[int(step/interval_steps)] = current_T


    for step in range(0, total_cooling_steps):
        sim_time += timestep
        # Initialization
        if step == 0:
            cooling_temps = np.zeros(int(total_cooling_steps/interval_steps)) * u.kelvin
            cooling_temps[0] = current_T
            freq = pyrex.init_freq_dict(t_pairs[0]._value, t_pairs[1]._value,
                                                dT._value, T_init=current_T._value)
        # Attempt to drop the RWMD ceiling temperature
        if step % cooling_rate_steps  == 0 and t_pairs[1] > t_pairs[0] + dT:
            if t_pairs[1] > t_pairs[0] + dT:
                t_pairs[1] -= dT
            if t_pairs[1] < current_T:
                current_T = t_pairs[1]
            freq = pyrex.init_freq_dict(t_pairs[0]._value, t_pairs[1]._value,
                                            dT._value, T_init=current_T._value)
        # Attempt to change temperature
        if step % interval_steps == 0:
            current_T = pyrex.choose_next_T(freq, current_T._value, 
                                            dT._value) * u.kelvin
            cooling_temps[int(step/interval_steps)] = current_T
            
    all_temps = np.append(heating_temps, cooling_temps) * u.kelvin
    return all_temps


def _validate_units(current_T, timestep, dT, heating_duration, interval_duration,
                    t_pairs, cooling_rate):
    if not (current_T.unit.is_compatible(u.kelvin) and 
            timestep.unit.is_compatible(u.femtoseconds) and 
            dT.unit.is_compatible(u.kelvin) and 
            heating_duration.unit.is_compatible(u.picoseconds) and 
            interval_duration.unit.is_compatible(u.picoseconds) and 
            t_pairs.unit.is_compatible(u.kelvin) and 
            cooling_rate.unit.is_compatible(u.picosecond/u.kelvin)):
            sys.exit("Double check your units for RWMD")


if __name__ == "__main__":
    main()
    
