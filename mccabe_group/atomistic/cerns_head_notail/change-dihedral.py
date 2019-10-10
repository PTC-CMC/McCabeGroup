import numpy as np


to_delete = range(5, 11) + range(23, 33)
angles_to_print = []
angles = np.loadtxt('dihedrals.txt', dtype='int')
for atype, ai, aj, ak, al in angles:
    if(ai not in to_delete and aj not in to_delete and ak not in to_delete and al not in
    to_delete):
        angles_to_print.append([atype, ai, aj, ak, al])
        for i, indices in enumerate(angles_to_print[-1][1:]):
            if indices >= 11:
                angles_to_print[-1][i+1] -= 6

np.savetxt('dihedrals-new.txt', np.asarray(angles_to_print), fmt='%d')
