import numpy as np


import mbuild as mb

##################################
## Some operations for operating on mBuild compounds
#################################

def align_cmpd(cmpd, align_indices):
    """ Align a compound

    Parameters
    ----------
    cmpd : mb.Compound
    align_indices : 2-tuple
        Cmpd.children indices to define molecule vector

    Returns
    -------
    aligned_cmpd : mb.Compound

    Notes
    -----
    Tail tip (first particle)is centered at origin.
    Headgroup (last particle) at most positive Z.
    Molecule aligned parallel to Z-axis
    """
    aligned_cmpd = mb.clone(cmpd)
    
    # Translate back to origin
    aligned_cmpd.translate(-1*aligned_cmpd.children[align_indices[0]].pos)
    
    # Define vectors
    cmpd_vector = (aligned_cmpd.children[align_indices[1]].pos
                  -aligned_cmpd.children[align_indices[0]].pos)
    ref_vector = [0,0,1]
    
    # Utilize dot products to compute angle between vectors
    # Utilize cross products to compute the vector normal to the
    # plane formed by the two vectors
    theta = mb.coordinate_transform.angle(cmpd_vector, ref_vector)
    normal = np.cross(cmpd_vector, ref_vector)

    # Rotate around a vector
    aligned_cmpd.rotate(theta, normal)

    # Translate back to origin
    aligned_cmpd.translate(-1*aligned_cmpd.children[align_indices[0]].pos)

    # If the compound is aligned along negative Z, reflect across XY plane
    if aligned_cmpd.pos[2] < 0:
        for particle in aligned_cmpd.particles():
            particle.pos[2] = -particle.pos[2]

    return aligned_cmpd
    
def write_compound_py(molecule_name, structure_file):
    """ Write compound python module for mbuild import

    Parameters
    ----------
    molecule_name : str
        Name of molecule
    structure_file : str
        filename to structure that contains xyz and bonding
        """
    with open('{}.py'.format(molecule_name), 'w') as f:
        f.write("""import mbuild as mb
class {0}(mb.Compound):
    def __init__(self):
        super({0},self).__init__()
        mb.load('{1}', compound=self, relative_to_module=self.__module__)""".format(
            molecule_name, structure_file))

