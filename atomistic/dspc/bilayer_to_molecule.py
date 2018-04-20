import mbuild as mb
import scripts.xml_utils as xml_utils
import scripts.itp_utils as itp_utils
import pdb

bilayer = mb.load('npt.pdb')
molecule = bilayer.children[0]

cmpd = itp_utils.compound_from_itp('dspc.itp')
cmpd = itp_utils.coordinates_from_compound(molecule, cmpd, a_to_nm=False)
aligned_cmpd = xml_utils.align_cmpd(cmpd, [89,50])

aligned_cmpd.save('{}.mol2'.format(aligned_cmpd.name), 
        residues=[aligned_cmpd.name], overwrite=True)


xml_utils.write_compound_py(aligned_cmpd.name, '{}.mol2'.format(aligned_cmpd.name))
