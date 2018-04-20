import numpy as np

import mbuild as mb

import scripts.bilayer as bilayer
import atomistic.ecer2_hairpin.ecer2 as ecer2
import atomistic.c24ffa.ffa24 as ffa24
import atomistic.tip3p.tip3p as tip3p


n_x = 8
n_y = 8
n_solvent_per_lipid = 20
leaflet_info = [ (ecer2.ecer2(), 32, 0),
                 (ffa24.ffa24(), 32, -0.5)
                 ]

top_layer = bilayer.make_leaflet(leaflet_info, spacing=0.50, n_x=n_x, n_y=n_y)
top_layer = bilayer.solvate_leaflet(top_layer, tip3p.HOH(), 
        density=900, n_compounds=n_solvent_per_lipid * n_x * n_y)

bot_layer = bilayer.make_leaflet(leaflet_info, spacing=0.50, n_x=n_x, n_y=n_y)
bot_layer = bilayer.solvate_leaflet(bot_layer, tip3p.HOH(), 
        density=900, n_compounds=n_solvent_per_lipid * n_x * n_y)
bot_layer = bilayer.reflect(bot_layer)



system = mb.Compound()
system.add(top_layer)
system.add(bot_layer)

system = bilayer.translate_to_positive_octant(system)

system.save('test.gro', box=system.boundingbox, 
        overwrite=True, residues=['ecer2', 'ffa24', 'HOH'])
