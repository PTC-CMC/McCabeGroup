import pdb
import numpy as np

import mbuild as mb
from mbuild.formats.lammpsdata import write_lammpsdata

import scripts.bilayer as bilayer

# Import statements for molecule prototypes
import atomistic.dppc.DPPC as DPPC
import atomistic.c24ffa.ffa24 as ffa24
import atomistic.tip3p.SOL as SOL

###################
## Sample script to construct and save an mBuild Bilayer for Gromacs
####################

# Bilayer specifications
filename = 'test'
path_to_ff = "#include \"/raid6/homes/ahy3nz/Programs/McCabeGroup/atomistic/forcefield.itp\""
apl = 0.50
tilt_angle = np.deg2rad(30)
solvent_density = 900
random_spin=np.deg2rad(10)
n_x = 4
n_y = 4
n_solvent_per_lipid = 5
leaflet_info = [ (DPPC.DPPC(), 8, 0),
                 (ffa24.ffa24(), 8, -0.5)
                 ]

system = bilayer.Bilayer(leaflet_info=leaflet_info, n_x=n_x, n_y=n_y, apl=apl, 
        tilt_angle=tilt_angle, random_spin=random_spin,
        solvent=SOL.SOL(), solvent_density=solvent_density, 
        n_solvent_per_lipid=n_solvent_per_lipid)

system = bilayer.translate_to_positive_octant(system)

# In order to avoid using smarts, define custom elements in parmed
# by adding underscores to mb particle names
for i in system.particles():
    i.name = "_{}".format(i.name)

structure = system.to_parmed(box=system.boundingbox, residues=set([p.parent.name for p in system.particles()]))


from foyer import Forcefield
ff = Forcefield(forcefield_files=['foyer_water.xml', 'foyer_charmm.xml'])
structure = ff.apply(structure)

# Because mbuild compounds don't pass charges to parmed structures, need to
# manuallly set the charges AFTER the force field has been applied
for i, j in zip(system.particles(), structure.atoms):
    j.charge = i.charge

pdb.set_trace()
write_lammpsdata(structure, 'thing.lammps')

#system.save('{}.gro'.format(filename), box=system.boundingbox, 
#        overwrite=True, residues=set([p.parent.name for p in system.particles()]))
#bilayer.write_gmx_topology(system, '{}.top'.format(filename), header=path_to_ff)
