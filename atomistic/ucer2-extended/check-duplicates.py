import numpy as np
dihedrals = np.loadtxt('dihedrals.txt', dtype='int')
for row in dihedrals:
    if np.unique(row[1:]).size != row[1:].size:
        print row
