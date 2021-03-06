import scripts.xml_utils as xml_utils
import mbuild as mb
import pdb

#########################
## This is a code to generate an mBuild compound from prototype.xml
## While the prototype.xml may not be properly aligned,
## the resulting mBuild compound is aligned
## Tail tip is origin, headgroup at highest Z coordinate
#######################
xmlfile = "cer-eos-hairpin.xml"
molecule_name = "cer1"
structure_file = molecule_name + ".mol2"
cmpd = xml_utils.compound_from_xml(xmlfile, a_to_nm=True, name=molecule_name)

# Perform aligning 
cmpd = xml_utils.align_cmpd(cmpd, align_indices=[24,195])

# Save structure and bonding information
cmpd.save('{}'.format(structure_file), overwrite=True, residues=[molecule_name])

# Write compound.py file
xml_utils.write_compound_py(cmpd, structure_file)
