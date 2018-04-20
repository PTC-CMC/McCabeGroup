import numpy as np

import mbuild as mb

import scripts.bilayer as bilayer

# Import statements for molecule prototypes
import atomistic.ecer2_hairpin.ecer2 as ecer2
import atomistic.c24ffa.ffa24 as ffa24
import atomistic.tip3p.tip3p as tip3p

###################
## Sample script to construct and save an mBuild Bilayer for Gromacs
####################

# Bilayer specifications
filename = 'test'
path_to_ff = "#include /raid6/homes/ahy3nz/Programs/McCabeGroup/atomistic/forcefield.itp"
apl = 0.50
tilt_angle = np.deg2rad(30)
solvent_density = 900
random_spin=np.deg2rad(10)
n_x = 8
n_y = 8
n_solvent_per_lipid = 20
leaflet_info = [ (ecer2.ecer2(), 40, 0),
                 (ffa24.ffa24(), 24, -0.5)
                 ]

system = bilayer.Bilayer(leaflet_info=leaflet_info, n_x=n_x, n_y=n_y, apl=apl, 
        tilt_angle=tilt_angle, random_spin=random_spin,
        solvent=tip3p.HOH(), solvent_density=solvent_density, 
        n_solvent_per_lipid=n_solvent_per_lipid)

system = bilayer.translate_to_positive_octant(system)

system.save('{}.gro'.format(filename), box=system.boundingbox, 
        overwrite=True, residues=set([p.parent.name for p in system.particles()]))
bilayer.write_gmx_topology(system, '{}.top'.format(filename), header=path_to_ff)
