from lxml import etree as ET

# All the txt files we need to scrape
files = ['coords.txt', 'masses.txt', 'charges.txt', 'bonds.txt', 'angles.txt',
        'dihedrals.txt', 'impropers.txt']

# Maybe include a conversion from types.txt

# All the elements in this tree
prototype = ET.Element("prototype")
configuration = ET.SubElement(prototype, "configuration")
configuration.text="\nHELLLOO\n"
type_element = ET.SubElement(configuration, 'type')
position_element = ET.SubElement(configuration,'position')
bond_element = ET.SubElement(configuration,'bond')
angle_element = ET.SubElement(configuration,'angle')
mass_element = ET.SubElement(configuration,'mass')
charge_element = ET.SubElement(configuration,'charge')
dihedral_element = ET.SubElement(configuration,'dihedral')
improper_element = ET.SubElement(configuration,'improper')

#ET.SubElement(doc, "field1", name="blah").text = "some value1"
#ET.SubElement(doc, "field2", name="adfasdfasdfa").text = "some value2"

tree = ET.ElementTree(prototype)
tree.write('new.xml', pretty_print=True, xml_declaration=False)


