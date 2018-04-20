import mbuild as mb
from collections import OrderedDict
import numpy as np
import sys
from itertools import product

#######################
## This is a collection of functions used to build bilayers
######################

def make_leaflet(leaflet_info, n_x=8, n_y=8, tilt_angle=0, spacing=0, 
        random_z_displacement=0):
    """ Generate a leaflet by laying down molecules in a 2D grid at random grid points

    Parameters
    ---------
    n_x : int
        2D grid dimension
    n_y : int
        2D grid dimension
    leaflet_info : n x 3 array
        Each row corresponds to a molecule
        First column is the mB compound
        Second column is the number of that lipid
        Third column is a z-offset specific to molecules of that type
    tilt_angle : float
        tilt angle (spun around y-axis)
    spacing : float
        spacing between leaflets, based on area per lipid
    random_z_displacement : float (nm)
        Randomly offset molecules by a small amount
       
    Returns
    -------
    leaflet : mb.Compound()
        Leaflet of molecules
      
    """


    leaflet = mb.Compound()

    # Create ordered pairs
    ordered_pairs = []
    for i, j in product(range(n_x), range(n_y)):
        ordered_pairs.append((i,j))


    # Randomly assign ordered pairs to each lipid
    # based on the way lipids is set, all of one molecule is listed first
    # before getting to the next one
    # Loop through each type of molecule (DSPC, DPPC, etc.)
    for i, lipid_type in enumerate(leaflet_info):
        # Loop through the system's quantity of that particular molecule
        for n in range(lipid_type[1]):
            random_index = np.random.randint(0, len(ordered_pairs))
            (i, j) = ordered_pairs.pop(random_index)

            # Do geometry transformations
            molecule_to_add = mb.clone(lipid_type[0])
            # Apply tilt angle
            molecule_to_add.spin(tilt_angle, [0, 1, 0])

            # Apply z_offset
            z_offset = lipid_type[2]

            # Apply APL and z_offset to identify the position for the molecule in the grid
            position = [i * spacing, j * spacing, z_offset + 
                        (-1 * np.random.random() * random_z_displacement)]
            molecule_to_add.translate(position)

            # Add the new molecule to the leaflet
            leaflet.add(molecule_to_add)

    return leaflet

def reflect(leaflet):
    """ Reflect leaflet across XY plane """
    new_leaflet = mb.clone(leaflet)
    for particle in new_leaflet.particles():
        particle.pos[2] = -particle.pos[2]
    return new_leaflet

def solvate_leaflet(leaflet, solvent, **kwargs):
    """ Solvate a leaflet 

    Parameters
    ---------
    leaflet : mB.Compound()
    solvent : mB.Compound()
    **kwargs : for mb.fill_box()

    Notes
    -----
    Solvents placed at highest Z coordinate """

    solvent_box = mb.fill_box(solvent, **kwargs)
    top_of_leaflet = np.max([p.pos[2] for p in leaflet.particles()])
    bot_of_solvent = np.min([p.pos[2] for p in solvent_box.particles()])
    solvent_box.translate([0,0, top_of_leaflet - bot_of_solvent])

    leaflet.add(solvent_box)
    return layer
