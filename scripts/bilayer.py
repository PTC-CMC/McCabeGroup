import mbuild as mb
from collections import OrderedDict
from oset import oset as OrderedSet
import numpy as np
import sys
from itertools import product, groupby

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

            # Apply APL and z_offset to identify the position for the 
            # molecule in the grid
            position = [i * spacing, j * spacing, z_offset + 
                        (-1 * np.random.random() * random_z_displacement)]
            molecule_to_add.translate(position)

            # Add the new molecule to the leaflet
            leaflet.add(molecule_to_add)

    return leaflet

def reflect(leaflet):
    """ Reflect leaflet across XY plane """
    for particle in leaflet.particles():
        particle.pos[2] = -particle.pos[2]
    return leaflet

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
    top_of_leaflet = np.max(leaflet.xyz[:,2])
    bot_of_solvent = np.min(solvent.xyz[:,2])
    solvent_box.translate([0,0, top_of_leaflet - bot_of_solvent])

    leaflet.add(solvent_box)
    return leaflet

def translate_to_positive_octant(system):
    """ Shift all coordinates to positive xyz,
    useful for gromacs simulations"""
    to_translate = [-1*np.min(system.xyz[:,0]),
                -1*np.min(system.xyz[:,1]),
                -1*np.min(system.xyz[:,2])]
    system.translate(to_translate)
    return system

def random_orientation(leaflet, angle):
    """ Randomly spin lipids

    Parameters
    ----------
    leaflet : mB.Compound()
    angle : float, radians
    """
    for cmpd in leaflet.children:
        cmpd.spin((angle * np.random.random()) - (angle / 2), [0,0,1])
    return leaflet

def write_gmx_topology(system, filename, header=""):
    """ Write out gmx topology file 

    Parameters
    ----------
    system : mb.Compound()
    filename : str
    header : str, optional
        Header string for include statements etc

    Notes
    -----
    Molecule names are based on the one-level-up parents of the particles
        """
    molecules = OrderedSet()
    for p in system.particles():
        if p.parent is not None:
            molecules.add(p.parent)

    with open(filename,'w') as f:
        f.write("{}\n".format(header))
        f.write("\n".join(["{:<8s} {}".format(name, sum(1 for _ in g))
            for name,g in groupby([c.name for c in molecules])]))
