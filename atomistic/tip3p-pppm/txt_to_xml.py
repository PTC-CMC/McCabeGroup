from lxml import etree as ET
#################################
## This is a short code used to convert text files containing molecule parameters
## into XML files. While not all molecule parameters may be present (i.e.
## coarse-grained molecules do not have dihedrals), the basic functions are in place
## to read a text file and move that text into an XML element
## that can then be printed in XML format
##################################

ATOMTYPES_FILE = 'elements.txt'

def _parse_type_dict(filename, zero_index=False):
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


def _write_type_position_elements(type_element, position_element, filename,
        atomtypes=None):
    """ Given a filename with type and coordinates, print to respective XML element
   
    Parameters
    ----------
    type_element : ET.SubElement
        SubElement corresponding to the type element
    position_element : ET.SubElement
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

def _write_xml_elements(element, filename):
    """ Given a filename, print the contents to that XML element"""
    element.text = "\n"
    all_lines = open(filename, 'r').readlines()
    for line in all_lines:
        line = line.rstrip()
        element.text += "{}\n".format(line)

if __name__ == "__main__":
    # All the txt files we need to scrape
    #files = ['coords.txt', 'masses.txt', 'charges.txt', 'bonds.txt', 'angles.txt',
            #'dihedrals.txt', 'impropers.txt']
    
    # Conversion from types.txt
    atomtypes = None
    if ATOMTYPES_FILE is not None:
        atomtypes = _parse_type_dict(ATOMTYPES_FILE, zero_index=False)
    
    # All the elements in this tree
    prototype = ET.Element("prototype")
    configuration = ET.SubElement(prototype, "configuration")
    
    type_element = ET.SubElement(configuration, 'type')
    position_element = ET.SubElement(configuration,'position')
    _write_type_position_elements(type_element, position_element, 'coords.txt',
            atomtypes=atomtypes)
    
    bond_element = ET.SubElement(configuration,'bond')
    _write_xml_elements(bond_element, 'bonds.txt')
    
    angle_element = ET.SubElement(configuration,'angle')
    _write_xml_elements(angle_element, 'angles.txt')
    
    mass_element = ET.SubElement(configuration,'mass')
    _write_xml_elements(mass_element, 'masses.txt')
    
    charge_element = ET.SubElement(configuration,'charge')
    _write_xml_elements(charge_element, 'charges.txt')
    
    #dihedral_element = ET.SubElement(configuration,'dihedral')
    #_write_xml_elements(dihedral_element, 'dihedrals.txt')
    
    #improper_element = ET.SubElement(configuration,'improper')
    #_write_xml_elements(improper_element, 'impropers.txt')
    
    
    # Construct the tree and print to file
    tree = ET.ElementTree(prototype)
    tree.write('tip3p-pppm.xml', pretty_print=True, xml_declaration=False)
    
    
