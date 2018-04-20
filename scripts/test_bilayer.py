import numpy as np

import mbuild as mb

import scripts.bilayer as bilayer
import atomistic.ecer2_hairpin.ecer2 as ecer2
import atomistic.c24ffa.ffa24 as ffa24
import atomistic.tip3p.tip3p as tip3p


apl = 0.50
tilt_angle = np.deg2rad(30)
solvent_density = 900
random_spin=np.deg2rad(0)
n_x = 8
n_y = 8
n_solvent_per_lipid = 20
leaflet_info = [ (ecer2.ecer2(), 64, 0),
                 (ffa24.ffa24(), 0, -0.5)
                 ]
system = bilayer.Bilayer(apl=apl, tilt_angle=tilt_angle,
        solvent=tip3p.HOH(), solvent_density=solvent_density, 
        random_spin=random_spin,
        n_x=n_x, n_y=n_y, n_solvent_per_lipid=n_solvent_per_lipid,
        leaflet_info=leaflet_info)

system = bilayer.translate_to_positive_octant(system)

system.save('test.gro', box=system.boundingbox, 
        overwrite=True, residues=set([p.parent.name for p in system.particles()]))
bilayer.write_gmx_topology(system, 'test.top', header='#include stuff')
