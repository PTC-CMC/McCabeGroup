import unyt as u
import numpy as np
from foyer import Forcefield

import mbuild as mb
from mbuild.formats.hoomdxml import write_hoomdxml

from cg.prototypes.DSPC import DSPC
from scripts.randomized_membrane import Randomized_Membrane

PATH_TO_FF = '/raid6/homes/ahy3nz/Programs/setup/FF/CG/msibi_ff.xml'
if __name__ == "__main__":
    leaflet_info = [ (DSPC(), 64)]
    system = Randomized_Membrane(leaflet_info)
    structure = system.to_parmed(box=system.boundingbox)

    ff = Forcefield(forcefield_files=PATH_TO_FF)
    kwargs  = {}
    kwargs['rigid_bodies'] = [p.rigid_id for p in system.particles()]
    structure = ff.apply(structure, assert_dihedral_params=False)
    write_hoomdxml(structure, 'packed.hoomdxml', shift_coords=False,
            ref_energy=0.239, ref_distance=10, **kwargs)

