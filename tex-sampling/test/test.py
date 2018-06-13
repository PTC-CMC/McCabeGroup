import pdb

import matplotlib.pyplot as plt
import numpy as np

import pyrex.pyrex as pyrex

# initialize temperature
current_T = 305.0
dT = 5.0
T_freq = pyrex.init_freq_dict(305.0, 400.0, dT, T_init=current_T)
T_visited = open('T-visited.txt', 'a')
T = []

for i in range(10000):
    T_visited.write('%.1f\n' % current_T)
    T.append(current_T)
    #run_lammps('in.cer1.lmp', current_T)
    current_T = pyrex.choose_next_T(T_freq, current_T, dT)
fig, ax = plt.subplots(nrows=2, sharex=False)
T_hist, bins = np.histogram(T, bins=len(T_freq.keys()), normed=True)
ax[0].plot(bins[:-1], T_hist)
ax[0].set_ylim(bottom=0, top=np.amax(T_hist) * 1.1)
ax[1].plot(T)
ax[0].set_xlabel('T')
ax[1].set_xlabel('TEX step')
ax[0].set_ylabel('f(T)')
ax[1].set_ylabel('T')
plt.show()
