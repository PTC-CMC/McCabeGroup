import numpy as np


to_delete = range(5, 15) + range(19, 75)
angles_to_print = []
angles = np.loadtxt('coords.txt')
for i, line in enumerate(angles):
    if i not in to_delete:
        angles_to_print.append(line)


np.savetxt('coords-new.txt', np.asarray(angles_to_print), fmt='%d %.4f %.4f %.4f')
