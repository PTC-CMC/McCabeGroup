import pdb
from lxml import etree
import numpy as np

#KJ_TO_KCAL = 0.239
#NM_TO_A = 10

# Units from the chodera group were in agreement with foyer/openmm units
# leave everything in terms of kj and nm, but I'm too lazy to modify the 
# functions below, so i'm leaving the conversions here
KJ_TO_KCAL = 1
NM_TO_A = 1


# This code is supposed to modify the charmm36.xml code from the Chodera group
# In a format suitable for Foyer
# Note that this xml has some additional atomtypes specified from Tim's parameters

#tree = etree.parse('charmm36_nowaters.xml')
tree = etree.parse('waters_ions_default.xml')
root = tree.getroot()
# All the relevant XML elements
atomTypes = root.findall('AtomTypes')[0]
harmonicBondForce = root.findall('HarmonicBondForce')[0]
harmonicAngleForce = root.findall('HarmonicAngleForce')[0]
nonbondedForce = root.findall('NonbondedForce')[0]
lennardJonesForce = root.findall("LennardJonesForce")[0]

new_root = etree.Element('ForceField')
# Atomtypes
for type_element in atomTypes:
    # Need to add underscores for all elements and definitions
    # This is to avoid having to use SMARTS to atomtype a system
    # Similar to CG methodology for forcefields
    if type_element.attrib['name'] != 'ZN':
        type_element.attrib['def'] = "[_{}]".format(type_element.attrib['name'])
        type_element.attrib['element'] = "_{}".format(type_element.attrib['name'])
    else:
        atomTypes.remove(type_element)
new_root.append(atomTypes)


# Bonds
for bond_element in harmonicBondForce:
    # Do unit conversions for them all
    bond_element.attrib['k'] = "{:15.5f}".format( KJ_TO_KCAL * (NM_TO_A **-2) *\
                                float(bond_element.attrib['k'])).strip()
    bond_element.attrib['length']="{:7.4f}".format(NM_TO_A * \
                                   float(bond_element.attrib['length'])).strip()
new_root.append(harmonicBondForce)

# Angles
for angle_element in harmonicAngleForce:
    angle_element.attrib['k'] = "{:15.5f}".format(KJ_TO_KCAL *  \
                                float(angle_element.attrib['k'])).strip()
    angle_element.attrib['angle'] = "{:15.5f}".format(\
                                    float(angle_element.attrib['angle'])).strip()
new_root.append(harmonicAngleForce)


# LJ force terms move into the nonbondedforce terms
for nonbond_element in nonbondedForce:
    # Look through each nonbonded force
    if nonbond_element.tag != "UseAttributeFromResidue" and \
       nonbond_element.attrib['type'] != "ZN":
        for lj_element in lennardJonesForce:
        # Find the lennard jones force with the associated type
            if nonbond_element.tag=="Atom" and lj_element.tag=="Atom":
                if nonbond_element.attrib['type'] == lj_element.attrib['type']:
                    nonbond_element.attrib['sigma'] = lj_element.attrib['sigma']
                    nonbond_element.attrib['epsilon'] = lj_element.attrib['epsilon']
                    nonbond_element.attrib['charge'] = "0.0"
    else:
        nonbondedForce.remove(nonbond_element)

new_root.append(nonbondedForce)
# Construct tree and save
new_tree = etree.ElementTree(new_root)
new_tree.write("foyer_water.xml", pretty_print=True)
