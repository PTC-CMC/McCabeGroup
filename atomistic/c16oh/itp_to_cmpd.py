import mbuild as mb
import scripts.xml_utils as xml_utils
import scripts.itp_utils as itp_utils
import pdb


#######################
## Example script to convert an ITP file into an mBuild compound python module
## Note that the xyz coordinates must be pulled from another file
####################

ref_molecule = mb.load('oh16.pdb')
#molecule = bilayer.children[0]

cmpd = itp_utils.compound_from_itp('oh16.itp')
cmpd = itp_utils.coordinates_from_compound(ref_molecule, cmpd)
aligned_cmpd = xml_utils.align_cmpd(cmpd, [24,46])

aligned_cmpd.save('{}.mol2'.format(aligned_cmpd.name), 
        residues=[aligned_cmpd.name], overwrite=True)


xml_utils.write_compound_py(aligned_cmpd.name, '{}.mol2'.format(aligned_cmpd.name))
