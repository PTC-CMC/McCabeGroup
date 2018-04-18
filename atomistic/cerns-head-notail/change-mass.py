import numpy as np


to_delete = range(5, 11) + range(23, 33)
angles_to_print = []
angles = np.loadtxt('masses.txt')
for i, line in enumerate(angles):
    if i not in to_delete:
        angles_to_print.append(line)


np.savetxt('masses-new.txt', np.asarray(angles_to_print), fmt='%.4f')
