import scripts.xml_utils as xml_utils
import mbuild as mb

#########################
## This is a code to generate and mBuild compound from 
## a prototype.xml
#######################
xmlfile = ""
cmpd = xml_utils.compound_from_xml(xmlfile, a_to_nm=True)
cmpd.save('.mol2', overwrite=True)
