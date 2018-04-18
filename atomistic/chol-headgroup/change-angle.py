import numpy as np


to_delete = range(5, 15) + range(19, 75)
angles_to_print = []
angles = np.loadtxt('angles.txt', dtype='int')
for atype, ai, aj, ak in angles:
    if ai not in to_delete and aj not in to_delete and ak not in to_delete:
        angles_to_print.append([atype, ai, aj, ak])
        for i, indices in enumerate(angles_to_print[-1][1:]):
            if indices >= 15:
                angles_to_print[-1][i+1] -= 10

np.savetxt('angles-new.txt', np.asarray(angles_to_print), fmt='%d')
