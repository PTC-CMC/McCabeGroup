import numpy as np
import datetime
import scripts.itp_utils as itp_utils
import pdb

###########
## This script is used to modify an itp file by keeping only lines
## that contain the relevant atom indices
##########

def _is_valid(atoms, valid_indices):
    """ Check if a given group of atoms matches the indices we want to keep 

    Parameters
    ---------
    atoms : list
    valid_indices : list

    Returns
    -------
    valid : True if all the atoms are within the valid indices
    """
    for atom_index in atoms:
        if atom_index not in valid_indices:
            return False

    return True

valid_indices = np.concatenate((np.arange(1,48), np.arange(88,91)))
valid_indices = ['{}'.format(val) for val in valid_indices]
renumber_indices = {"88": "48", "89":"49", "90":"50"}

original_itp = open('dppc.itp', 'r').readlines()
itplines = itp_utils.remove_comments(original_itp)
newitp = []

newitp.append('; Made by alex on {}\n'.format(datetime.datetime.now()))
newitp.append('[ moleculetype ]\n')
newitp.append(' ; name	nrexcl\n')
newitp.append('pchd      3\n')

atoms_section = itp_utils.read_section('atoms', itplines)
newitp.append('[ atoms ]\n')
newitp.append('; nr	type	resnr	residu	atom	cgnr	charge	mass\n')

for line in atoms_section:
    first = line.split()[0]
    if _is_valid([first], valid_indices):
        newline = line.split()
        if newline[0] in renumber_indices:
            newline[0] = renumber_indices[newline[0]]
        if newline[5] in renumber_indices:
            newline[5] = renumber_indices[newline[5]]

        line = "{:6}{:6}{:6}{:6}{:6}{:6}{:8}{:8}".format(*newline)
        newitp.append(line+"\n")

bond_section = itp_utils.read_section('bonds', itplines)
newitp.append('[ bonds ]\n')
newitp.append('; ai	aj	funct	b0	Kb\n')

for line in bond_section:
    first, second = line.split()[0], line.split()[1]
    if _is_valid([first,second], valid_indices):
        newline = line.split()
        if newline[0] in renumber_indices:
            newline[0] = renumber_indices[newline[0]]
        if newline[1] in renumber_indices:
            newline[1] = renumber_indices[newline[1]]

        line = "   ".join(newline)

        newitp.append(line+"\n")

pairs_section = itp_utils.read_section('pairs', itplines)
newitp.append('[ pairs ]\n')
newitp.append('; ai	aj	funct	c6	c12\n')

for line in pairs_section:
    first, second = line.split()[0], line.split()[1]
    if _is_valid([first,second], valid_indices):
        newline = line.split()
        if newline[0] in renumber_indices:
            newline[0] = renumber_indices[newline[0]]
        if newline[1] in renumber_indices:
            newline[1] = renumber_indices[newline[1]]

        line = "   ".join(newline)

        newitp.append(line+"\n")

angles_section = itp_utils.read_section('angles', itplines)
newitp.append('[ angles ] \n')
newitp.append('; ai	aj	ak	funct	th0	cth	S0	Kub\n')

for line in angles_section:
    first, second, third = line.split()[0], line.split()[1], line.split()[2]
    if _is_valid([first,second, third], valid_indices):
        newline = line.split()
        if newline[0] in renumber_indices:
            newline[0] = renumber_indices[newline[0]]
        if newline[1] in renumber_indices:
            newline[1] = renumber_indices[newline[1]]
        if newline[2] in renumber_indices:
            newline[2] = renumber_indices[newline[2]]


        line = "   ".join(newline)

        newitp.append(line+"\n")

dihedrals_section = itp_utils.read_section('dihedrals', itplines)
newitp.append('[ dihedrals ]\n')
newitp.append('; ai	aj	ak	al	funct	phi0	cp	mult\n')

for line in dihedrals_section:
    first, second, third, fourth = line.split()[0], line.split()[1], \
                                   line.split()[2], line.split()[3]
    if _is_valid([first,second, third,fourth], valid_indices):
        newline = line.split()
        if newline[0] in renumber_indices:
            newline[0] = renumber_indices[newline[0]]
        if newline[1] in renumber_indices:
            newline[1] = renumber_indices[newline[1]]
        if newline[2] in renumber_indices:
            newline[2] = renumber_indices[newline[2]]
        if newline[3] in renumber_indices:
            newline[3] = renumber_indices[newline[3]]



        line = "   ".join(newline)

        newitp.append(line+"\n")

# Fortunately, the impropers section requires no extra work, so manualy add
newitp.append('[ dihedrals ]\n')
newitp.append('; ai	aj	ak	al	funct	q0	cq\n')
newitp.append('   31    30    33    32     2\n')
newitp.append('   40    39    42    41     2\n')

with open('pchd.itp', 'w') as f:
    for line in newitp:
        f.write(line)
