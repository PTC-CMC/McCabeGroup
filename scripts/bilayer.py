import mbuild as mb
from collections import OrderedDict
import numpy as np
import sys
from itertools import product

#######################
## This is a collection of functions used to build bilayers
######################

def make_leaflet(n_x=8, n_y=8, lipid_system_info=None, tilt_angle=0, spacing=0, 
        random_z_displacement=0):
    """ Generate a leaflet by laying down molecules in a 2D grid at random grid points

    Parameters
    ---------
    n_x : int
        2D grid dimension
    n_y : int
        2D grid dimension
    lipid_system_info : n x 3 array
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
    for i, lipid_type in enumerate(lipid_system_info):
        n_molecule_per_leaflet = int(lipid_type[1]/2)
        # Loop through the system's quantity of that particular molecule
        for n in range(n_molecule_per_leaflet):
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

