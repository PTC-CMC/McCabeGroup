import time
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
## Sample script to convert a GROMACS structure to a 
## fully-parameterized LAMMPS system
####################


system = mb.Compound()
for i in range(72):
    system.add(DPPC.DPPC())

for i in range(2160):
    system.add(SOL.SOL())
system.update_coordinates('wrapped.gro')


# In order to avoid using smarts, define custom elements in parmed
# by adding underscores to mb particle names
for num, i in enumerate(system.particles()):
    i.name = "_{}".format(i.name)

structure = system.to_parmed(box=system.boundingbox, residues=set([p.parent.name for p in system.particles()]))


from foyer import Forcefield
ff = Forcefield(forcefield_files=['foyer_water.xml', 'foyer_charmm.xml'])
start = time.time()
structure = ff.apply(structure, assert_dihedral_params=False)
end = time.time()
print("Applying FF took: {}".format(end-start))

# Because mbuild compounds don't pass charges to parmed structures, need to
# manuallly set the charges AFTER the force field has been applied
for i, j in zip(system.particles(), structure.atoms):
    j.charge = i.charge

start = time.time()
write_lammpsdata(structure, 'thing.lammps')
end = time.time()
print("Writing lammps structure took: {}".format(end-start))


