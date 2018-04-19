import numpy as np
import ipdb

def fix_bonds(name, deleted_atoms):
    bonds = np.loadtxt('{0}.txt'.format(name), dtype=np.int)
    new_bonds = []
    for bond in bonds:
        use = True
        for atom in bond[1:]: 
            if atom in deleted_atoms:
                use = False
                break
        if use:
            new_bond = [bond[0]]
            for atom in bond[1:]:
                if atom > 49:
                    new_bond.append(atom-24)
                else:
                    new_bond.append(atom)
            new_bonds.append(new_bond)
    new_bonds = np.asarray(new_bonds)
    np.savetxt('new-{0}.txt'.format(name), new_bonds, fmt='%d')

deleted_atoms = range(50, 73+1)
for bond in ['bonds', 'angles', 'dihedrals', 'impropers']:
    fix_bonds(bond, deleted_atoms)
