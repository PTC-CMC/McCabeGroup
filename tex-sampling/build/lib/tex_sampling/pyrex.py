import os
import cPickle as pickle
import random
import math
import pdb

import numpy as np

def choose_next_T(freqs, T_current, dT):
    """ Function to choose new temperature based on the sampled temperature 
    distribution.

    Args:
        freqs: dict with {T: n}, gives the sampled temperature distribution
        T_current: current temperature
        dT: spacing between temperature windows

    This function talks a step in a random direction in temperature space.
    It is written such that a flat temperature distribution is achieved. 
    """
    if T_current == min(freqs.keys()):
        shift = random.randint(0, 1)
    elif T_current == max(freqs.keys()):
        shift = random.randint(-1, 0)
    else:
        shift = random.randint(-1, 1)

    T_try = T_current + shift * dT

    if freqs[T_try] <= freqs[T_current]:
        T_new = T_try

    else:   # freqs[T_current] < freqs[T_try]
        q = math.exp(freqs[T_current] - freqs[T_try])   # on interval (0, 1]
        r = random.random()
        if r < q:
            T_new = T_try
        else:
            T_new = T_current

    freqs[T_new] += 1
    return T_new


def run_lammps(script, T, lammps_executable='lmp_edison', temp_var='T',
       parallel_command='aprun -n ', n_cores=24, outputfile='run.log'):
    os.system('%s %d %s -in %s -var %s %.1f > %s' %
            (parallel_command, n_cores, lammps_executable, script, 
                temp_var, T, outputfile))

def init_freq_dict(T_min, T_max, dT, T_init=None):
    num = (T_max - T_min) / dT + 1
    T_freq = dict.fromkeys(np.linspace(T_min, T_max, num=num), 0)
    if T_init:
        T_freq[T_init] += 1
    return T_freq

def load_freq_dict(picklefile):
    return 0 
