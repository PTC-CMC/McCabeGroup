import numpy as np

from lxml import etree
import xml.etree.ElementTree as ET

import mbuild as mb

#########################
## These are some useful python modules for converting between prototypes 
## that have been stored in a variety of formats
########################

ATOMTYPES_FILE_PATH = '/raid6/homes/ahy3nz/Programs/McCabeGroup/atomistic/types.txt'
def ATOMTYPES_FILE():
    return ATOMTYPES_FILE_PATH

def parse_type_dict(filename, zero_index=False):
    """ Read atomtypes into a list

    Parameters
    ----------
    filename : str
        Filename ot read types
    zero_index : bool, default False
        If True, first atomtype is stored in index 0
        If False, first atomtype is stored in index 1

    Returns
    -------
    atomtypes : list
        List of atomtypes

    Notes
    -----
    By default, we assume that each line has 2 elements,
    the index and the atomtype
        """
    all_lines = open(filename,'r').readlines()
    atomtypes = []
    if not zero_index: 
        atomtypes.append("NULL")
    for line in all_lines:
        line = line.rstrip()
        atomtypes.append(line.split()[1])
    return atomtypes


def write_type_position_elements(type_element, position_element, filename,
        atomtypes=None):
    """ Given a filename with type and coordinates, print to respective XML element
   
    Parameters
    ----------
    type_element : lxml.etree.SubElement
        SubElement corresponding to the type element
    position_element : lxml.etree.SubElement
        SubElement corresponding to the position element
    filename : str
        Filename with coords and types
        This file is assumed to have type, x, y, z on each line
    atomtypes : list
        If passed, will also specify the atomtype in the type element

    """
    type_element.text = "\n"
    position_element.text = "\n"
    coords = open(filename,'r').readlines()
    for line in coords:
        line = line.rstrip()
        atomtype_index, xyz = line.split()[0], line.split()[1:4]
        if atomtypes is not None:
            type_element.text += "{},{}\n".format(atomtype_index, 
                    atomtypes[int(atomtype_index)])
        else:
            type_element.text += "{}\n".format(atomtype_index)
        position_element.text += "{:<8.5f} {:<8.5f} {:<8.5f}\n".format(float(xyz[0]),
                float(xyz[1]), float(xyz[2]))

def write_xml_elements(element, filename):
    """ Given a filename, print the contents to that XML element"""
    element.text = "\n"
    all_lines = open(filename, 'r').readlines()
    for line in all_lines:
        line = line.rstrip()
        element.text += "{}\n".format(line)

def compound_from_xml(xmlfile, a_to_nm=True, **kwargs):
    """ Generate an mBuild compound from an xml file
    
    Parameters
    ----------
    xmlfile : str
        name of xml file
    a_to_nm : bool, default True
        If True, convert positions coordinates to nm from Angstrom
    **kwargs : 
        to pass to the cmpd that gets returned

    Returns
    -------
    mb.Compound

    Notes
    -----
    The xml file specifies many parameters, 
    but only the types, positions, and bonds are used
    for making mBuilid compounds

    """
    tree = ET.parse(xmlfile)
    prototype = tree.getroot()
    configuration = prototype.findall('configuration')[0]
    type_element = configuration.findall('type')[0]
    position_element = configuration.findall('position')[0]
    bond_element = configuration.findall('bond')[0]
    angle_element = configuration.findall('angle')[0]
    mass_element = configuration.findall('mass')[0]
    charge_element = configuration.findall('charge')[0]
    dihedral_element = configuration.findall('dihedral')[0]
    improper_element = configuration.findall('improper')[0]
    
    cmpd = mb.Compound(**kwargs)
    # Generate mbuild particles for each type
    all_types = type_element.text.strip('\n').split('\n')
    
    # Get xyz coordinates for each particle
    all_xyz = position_element.text.strip('\n').split('\n')
    for atomtype, xyz in zip(all_types, all_xyz):
        if ',' in atomtype:
            # If this atomtype has a comma, then the format is
            # atomtype_index, atomtype_name
            # Otherwise, just use the text returned by atomtype
            atomtype = atomtype.split(',')[1]
            particle_to_add = mb.Compound(name=atomtype, 
                    pos=xyz.split())
            # XML files are usually in Angstroms, so we need to convert to nm
            if a_to_nm:
                particle_to_add.pos /= 10
            cmpd.add(particle_to_add)
    
    # Specify the bond network 
    all_bonds = bond_element.text.strip('\n').split('\n')
    for bond_entry in all_bonds:
        bondtype, i, j = bond_entry.split()
        cmpd.add_bond((cmpd.children[int(i)], cmpd.children[int(j)]))
    
    return cmpd

def align_cmpd(cmpd, align_indices):
    """ Align a compound

    Parameters
    ----------
    cmpd : mb.Compound
    align_indices : 3-tuple
        Cmpd.children indices for axis transform

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
    # First put the molecule on the XZ plane
    mb.z_axis_transform(aligned_cmpd, 
            new_origin=aligned_cmpd.children[align_indices[0]], 
            point_on_z_axis=aligned_cmpd.children[align_indices[1]],
            point_on_zx_plane=aligned_cmpd.children[align_indices[2]])
    
    
    # Cross product
    cmpd_vector = aligned_cmpd.children[-1].pos - aligned_cmpd.children[0].pos
    cmpd_mag = np.sqrt(np.dot(cmpd_vector, cmpd_vector))
    ref_vector = [0,0,1]
    ref_mag  = 1
    rotation_vector = np.cross(cmpd_vector, ref_vector)
    sin_theta = rotation_vector/ (cmpd_mag * ref_mag)
    theta = np.arcsin(sin_theta)


    # Rotate around a vector
    aligned_cmpd.rotate(theta[0], [1,0,0])
    aligned_cmpd.rotate(theta[1], [0,1,0])
    aligned_cmpd.rotate(theta[2], [0,0,1])

    # Translate back to origin
    aligned_cmpd.translate(-1*aligned_cmpd.children[0].pos)
    

    return aligned_cmpd
    
    
    
