from lxml import etree

import scripts.itp_utils as itp_utils

########################
## This is a script to convert itp files into XML prototypes
## Useful for generating files compatible with the groupy code
########################

prototype = etree.Element("prototype")
configuration = etree.SubElement(prototype, "configuration")


itplines = open('dppc.itp', 'r').readlines()
itplines = itp_utils.remove_comments(itplines)
directives = itp_utils.find_directives(itplines)
for directive, section in directives.items():
    # take out the plural/punctuation
    new_element = etree.SubElement(configuration, directive[:-1])
    new_element.text ="\n"
    for line in section:
        # each line in the XML element should contain the number-type 
        # of that interaction (bondtype, angletype, dihedraltype) 
        # and the corresponding atom indices of that interaction (0-indexed)


    tree = etree.ElementTree(prototype)
    tree.write('dppc.xml', pretty_print=True, xml_declaration=False)




