import pdb
import numpy as np
from lxml import etree

# After generting an openmm xml from forcefield.itp using parmed
# Need to eliminate <UseAttributeFromResidue>
# Need to eliminate <Info>
# Need to add 0-charges to the nonbonded force
KJ_TO_KCAL = 0.239006

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse('forcefield_frompmd_raw.xml', parser)
root = tree.getroot()
info = root.findall('Info')[0]
nonbonded = root.findall('NonbondedForce')[0]
atomTypes = root.findall('AtomTypes')[0]
harmonicBondForce = root.findall("HarmonicBondForce")[0]
harmonicAngleForce = root.findall("HarmonicAngleForce")[0]
periodicTorsionForce = root.findall("PeriodicTorsionForce")[0]
customTorsionForce = root.findall("CustomTorsionForce")[0]

# Remove info elements
root.remove(info)
# Remove use attribute from residue elements
for node in nonbonded:
    if node.tag=='UseAttributeFromResidue':
        nonbonded.remove(node)
    else:
        node.attrib['charge'] = '0.0'

for type_element in atomTypes:
    # Need to add underscores for all elements and definitions
    # This is to avoid having to use SMARTS to atomtype a system
    # Similar to CG methodology for forcefields
    type_element.attrib['def'] = "[_{}]".format(type_element.attrib['name'])
    type_element.attrib['element'] = "_{}".format(type_element.attrib['name'])

# Add FFA bond
extra_bond = etree.Element('Bond')
extra_bond.attrib['k'] = "{:15.5f}".format(456056.0).strip()
extra_bond.attrib['length'] = "{:15.5f}".format(0.096).strip()
extra_bond.attrib['type1'] = "OCL"
extra_bond.attrib['type2'] = "HL"
harmonicBondForce.append(extra_bond)

# Add FFA angles
# OBL-CL-OCL
OBL_CL_OCL =  etree.Element("Angle")
OBL_CL_OCL.attrib['type1'] = 'OCL'
OBL_CL_OCL.attrib['type2'] = 'CL'
OBL_CL_OCL.attrib['type3'] = 'OBL'
OBL_CL_OCL.attrib['angle'] = str(np.deg2rad(125.9))
OBL_CL_OCL.attrib['k'] = '753.12'
harmonicAngleForce.append(OBL_CL_OCL)

# CL-OCL-HL
CL_OCL_HL =  etree.Element("Angle")
CL_OCL_HL.attrib['type1'] = 'CL'
CL_OCL_HL.attrib['type2'] = 'OCL'
CL_OCL_HL.attrib['type3'] = 'HL'
CL_OCL_HL.attrib['angle'] = str(np.deg2rad(115.0))
CL_OCL_HL.attrib['k'] = '460.24'
harmonicAngleForce.append(CL_OCL_HL)

# Add FFA dihedrals
#dih = etree.Element("Proper")
#dih.attrib['type1'] = 'HAL2'
#dih.attrib['type2'] = 'CTL2'
#dih.attrib['type3'] = 'CL'
#dih.attrib['type4'] = 'OBL'
#dih.attrib['periodicity1'] = '6'
#dih.attrib['phase1'] = str(np.deg2rad(180.0))
#dih.attrib['k1'] = '0'
#periodicTorsionForce.append(dih)
#
#dih = etree.Element("Proper")
#dih.attrib['type1'] = 'OBL'
#dih.attrib['type2'] = 'CL'
#dih.attrib['type3'] = 'OCL'
#dih.attrib['type4'] = 'HL'
#dih.attrib['periodicity1'] = '2'
#dih.attrib['phase1'] = str(np.deg2rad(180.0))
#dih.attrib['k1'] = str(8.5772 * KJ_TO_KCAL)
#periodicTorsionForce.append(dih)
#
#dih = etree.Element("Proper")
#dih.attrib['type1'] = 'CTL2'
#dih.attrib['type2'] = 'CTL2'
#dih.attrib['type3'] = 'CL'
#dih.attrib['type4'] = 'OCL'
#dih.attrib['periodicity1'] = '3'
#dih.attrib['phase1'] = str(np.rad2deg(0.0))
#dih.attrib['k1'] = str(0.79496 * KJ_TO_KCAL)
#periodicTorsionForce.append(dih)
#
#dih = etree.Element("Proper")
#dih.attrib['type1'] = 'HAL2'
#dih.attrib['type2'] = 'CTL2'
#dih.attrib['type3'] = 'CL'
#dih.attrib['type4'] = 'OCL'
#dih.attrib['periodicity1'] = '6'
#dih.attrib['phase1'] = str(np.rad2deg(180.0))
#dih.attrib['k1'] = str(0 * KJ_TO_KCAL)
#periodicTorsionForce.append(dih)
#
#dih = etree.Element("Proper")
#dih.attrib['type1'] = 'CTL2'
#dih.attrib['type2'] = 'CL'
#dih.attrib['type3'] = 'OCL'
#dih.attrib['type4'] = 'HL'
#dih.attrib['periodicity1'] = '2'
#dih.attrib['phase1'] = str(np.rad2deg(180.0))
#dih.attrib['k1'] = str(8.5772 * KJ_TO_KCAL)
#periodicTorsionForce.append(dih)
#
#
#
## Add FFA impropers
#imp = etree.Element("Improper")
#imp.attrib['type1'] = 'OBL'
#imp.attrib['type2'] = 'CTL2'
#imp.attrib['type3'] = 'OCL'
#imp.attrib['type4'] = 'CL'
#imp.attrib['k'] = str(167.31816 * KJ_TO_KCAL)
#imp.attrib['theta0'] = str(np.deg2rad(0.0))
#customTorsionForce.append(imp)
#
#imp = etree.Element("Improper")
#imp.attrib['type1'] = 'OCL'
#imp.attrib['type2'] = 'CTL2'
#imp.attrib['type3'] = 'OBL'
#imp.attrib['type4'] = 'CL'
#imp.attrib['k'] = str(167.31816 * KJ_TO_KCAL)
#imp.attrib['theta0'] = str(np.deg2rad(0.0))
#customTorsionForce.append(imp)






tree.write('forcefield_frompmd_update.xml', pretty_print=True)
