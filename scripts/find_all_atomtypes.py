import pdb
import os
import os.path
import glob as glob

import scripts.itp_utils as itp_utils
import scripts.xml_utils as xml_utils


atomtype_dict = xml_utils.parse_type_dict(xml_utils.ATOMTYPES_FILE())
curr_dir = os.getcwd()
atomtypes = []
# Iterate through all prottype folders, picking out the atomtypes from the itp file
all_folders = [thing for thing in os.listdir() if os.path.isdir(thing)]
for folder in all_folders:
    os.chdir(os.path.join(curr_dir, folder))
    itpfile = [thing for thing in os.listdir() if os.path.isfile(thing) \
            and 'itp' in thing[-4:]]

    if itpfile:
        itpfile = glob.glob('*.itp')[0]
        itplines = open(itpfile, 'r').readlines()
        itplines = itp_utils.remove_comments(itplines)
        atomtype_lines = itp_utils.read_section('atoms', itplines)
        for line in atomtype_lines:
            atomtypes.append(line.split()[1])

# Look for all the new and unique atomtypes
atomtypes = set(atomtypes)
atomtype_dict = set(atomtype_dict)
uniques = atomtypes - atomtype_dict
for i in sorted(list(uniques)):
    print(i)
    
