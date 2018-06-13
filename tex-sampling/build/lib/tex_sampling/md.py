import os


def run_lammps(script, T, lammps_executable='lmp_edison', temp_var='T',
       parallel_command='aprun -n ', n_cores=24, outputfile='run.log'):
    os.system('%s %d %s -in %s -var %s %.1f > %s' %
            (parallel_command, n_cores, lammps_executable, script, 
                temp_var, T, outputfile))
