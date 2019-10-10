from lxml import etree
import scripts.xml_utils as xml_utils

#################################
## This is a short code used to convert text files containing molecule parameters
## into XML files. While not all molecule parameters may be present (i.e.
## coarse-grained molecules do not have dihedrals), the basic functions are in place
## to read a text file and move that text into an XML element
## that can then be printed in XML format
##################################


if __name__ == "__main__":
    # All the txt files we need to scrape
    #files = ['coords.txt', 'masses.txt', 'charges.txt', 'bonds.txt', 'angles.txt',
            #'dihedrals.txt', 'impropers.txt']
    
    # Conversion from types.txt
    atomtypes = None
    #ATOMTYPES_FILE = xml_utils.ATOMTYPES_FILE()
    if xml_utils.ATOMTYPES_FILE() is not None:
        atomtypes = xml_utils.parse_type_dict(xml_utils.ATOMTYPES_FILE(), 
                zero_index=False)
    
    # All the elements in this tree
    prototype = etree.Element("prototype")
    configuration = etree.SubElement(prototype, "configuration")
    
    type_element = etree.SubElement(configuration, 'type')
    position_element = etree.SubElement(configuration,'position')
    xml_utils.write_type_position_elements(type_element, position_element, 
            'coords.txt',
            atomtypes=atomtypes)
    
    bond_element = etree.SubElement(configuration,'bond')
    xml_utils.write_xml_elements(bond_element, 'bonds.txt')
    
    angle_element = etree.SubElement(configuration,'angle')
    xml_utils.write_xml_elements(angle_element, 'angles.txt')
    
    mass_element = etree.SubElement(configuration,'mass')
    xml_utils.write_xml_elements(mass_element, 'masses.txt')
    
    charge_element = etree.SubElement(configuration,'charge')
    xml_utils.write_xml_elements(charge_element, 'charges.txt')
    
    dihedral_element = etree.SubElement(configuration,'dihedral')
    xml_utils.write_xml_elements(dihedral_element, 'dihedrals.txt')
    
    improper_element = etree.SubElement(configuration,'improper')
    xml_utils.write_xml_elements(improper_element, 'impropers.txt')
    
    
    # Construct the tree and print to file
    tree = etree.ElementTree(prototype)
    tree.write('c16ffa_new.xml', pretty_print=True, xml_declaration=False)
    
    
