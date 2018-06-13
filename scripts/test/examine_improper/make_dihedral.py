import numpy as np
import pdb
import mbuild as mb
import DPPC

#dppc = DPPC.DPPC()
#system = mb.Compound()
#for i in [19,20,21,22,23,24,25]:
#    system.add(dppc.children[i])

system = mb.load('small.mol2')
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


