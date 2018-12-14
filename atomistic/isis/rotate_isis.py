import scripts.xml_utils as xml_utils
import scripts.itp_utils as itp_utils
import numpy as np
import mbuild as mb
import pdb

# Get the ISIS molecule from charmm-gui
#cmpd = mb.load('isis.gro')
#cmpd.name='ISIS'
#first_tail = cmpd.children[3:54]
#second_tail = [a for a in cmpd.children[55:109] if 'C' in a.name]

# Doing simple tail rotations
#ref_vector = second_tail[-1].xyz - second_tail[0].xyz
#cmpd_vector = first_tail[-1].xyz - first_tail[0].xyz
#
#theta = mb.coordinate_transform.angle(cmpd_vector[0], ref_vector[0])
#normal = np.cross(cmpd_vector[0], ref_vector[0])
#
#for a in first_tail:
#    a.rotate(theta-0.2, normal)
#cmpd.save('new_isis.gro', overwrite=True, residues='ISIS')

# Then run then run an EM

# Then reorient according to convention

cmpd = itp_utils.compound_from_itp("ISIS.itp")
coords = mb.load('em_nopbc.gro')
cmpd = itp_utils.coordinates_from_compound(coords, cmpd)
cmpd.name='ISIS'
first_tail = cmpd.children[3:54]
second_tail = [a for a in cmpd.children[55:109] if 'C' in a.name]
cmpd = xml_utils.align_cmpd(cmpd, [3, 51])
cmpd.save('isis.mol2',
        residues=[cmpd.name], overwrite=True)


xml_utils.write_compound_py(cmpd, 'isis.mol2')
