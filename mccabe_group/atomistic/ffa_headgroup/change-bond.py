import numpy as np


to_delete = range(0, 22) + range(27, 75)
angles_to_print = []
angles = np.loadtxt('bonds.txt', dtype='int')
for atype, ai, aj in angles:
    if ai not in to_delete and aj not in to_delete:
        angles_to_print.append([atype, ai, aj])
        for i, indices in enumerate(angles_to_print[-1][1:]):
            if indices >= 11:
                angles_to_print[-1][i+1] -= 22

np.savetxt('bonds-new.txt', np.asarray(angles_to_print), fmt='%d')
