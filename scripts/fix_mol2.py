import itp_utils as itp_utils
import mbuild as mb
import parmed as pmd


def from_itp_mol2(path, mol_name):
    """ Fix mol2 files that have atom type
        put in both the atom name and atom type fields
        
        Parameters
        ---------
        path : str
        mol_name : str
        
        Notes
        -----
        Will generate a new mol2 file with of the form
        {}_new.mol2
        """
    
    #itp_file = path + 'tip3p.itp'
    itp_file = path + mol_name + '.itp'
    mol2_file = path + mol_name + '.mol2'
    
    itplines = open(itp_file,'r').readlines()
    itplines = itp_utils.remove_comments(itplines)
    
    
    mol2_file_out = path + mol_name + "_new.mol2"
    
    cmpd2 = mb.load(mol2_file)
    cmpd2.name=mol_name
    

    #parmed won't read this mol2 file in properly directly
    temp_parmed = pmd.Structure()
    temp_parmed = cmpd2.to_parmed(residues=[cmpd2.name])

    atom_name_list = []
    atom_type_list = []

    #search for relavant info
    atoms_directive = itp_utils.find_directive('atoms', itplines)
    index = atoms_directive
    
    keep_iterating = True
    while keep_iterating == True:
        index += 1
        if itplines[index].find('bonds') == -1:
            
            atom_info = itplines[index].split(' ')
            
            if len(atom_info) >= 7:
                atom_name_list.append(atom_info[4])
                atom_type_list.append(atom_info[1])
        else:
            keep_iterating = False


    #set the properties in the parmed structure
    for i, atom in enumerate(temp_parmed):
        atom.name = atom_name_list[i]
        atom.type = atom_type_list[i]


    temp_parmed.save(mol2_file_out, overwrite=True)


path = '/Users/cri/Projects/McCabeGroup_repo/McCabeGroup/atomistic/pc_head/'
mol_name = 'pchd'


from_itp_mol2(path, mol_name)

