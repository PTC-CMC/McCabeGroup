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

tree = etree.parse('charmm36_nowaters.xml')
root = tree.getroot()
# All the relevant XML elements
atomTypes = root.findall('AtomTypes')[0]
harmonicBondForce = root.findall('HarmonicBondForce')[0]
harmonicAngleForce = root.findall('HarmonicAngleForce')[0]
ureyBradleyForce = root.findall("AmoebaUreyBradleyForce")[0]
periodicTorsionForce = root.findall("PeriodicTorsionForce")[0]
improperTorsionForce = root.findall("CustomTorsionForce")[0]
lennardJonesForce = root.findall("LennardJonesForce")[0]
nonbondedForce = root.findall('NonbondedForce')[0]

new_root = etree.Element('ForceField')
# Atomtypes
for type_element in atomTypes:
    # Need to add underscores for all elements and definitions
    # This is to avoid having to use SMARTS to atomtype a system
    # Similar to CG methodology for forcefields
    type_element.attrib['def'] = "[_{}]".format(type_element.attrib['name'])
    type_element.attrib['element'] = "_{}".format(type_element.attrib['name'])
new_root.append(atomTypes)


# Bonds
for bond_element in harmonicBondForce:
    # Negelct HT bonds since that should be handled in the water ffxml
    if bond_element.attrib['type1'] != 'HT' and \
       bond_element.attrib['type2'] != 'HT':
            bond_element.attrib['k'] = "{:15.5f}".format(\
                                        float(bond_element.attrib['k'])).strip()
            bond_element.attrib['length']="{:7.4f}".format( \
                                           float(bond_element.attrib['length'])).strip()
    else:
        harmonicBondForce.remove(bond_element)
# Define additiona lbond
extra_bond = etree.Element('Bond')
extra_bond.attrib['k'] = "{:15.5f}".format(456056.0).strip()
extra_bond.attrib['length'] = "{:15.5f}".format(0.096).strip()
extra_bond.attrib['type1'] = "OCL"
extra_bond.attrib['type2'] = "HL"
harmonicBondForce.append(extra_bond)
new_root.append(harmonicBondForce)

# Angles
for angle_element in harmonicAngleForce:
    angle_element.attrib['k'] = "{:15.5f}".format(KJ_TO_KCAL *  \
                                float(angle_element.attrib['k'])).strip()
    angle_element.attrib['angle'] = "{:15.5f}".format(\
                                    float(angle_element.attrib['angle'])).strip()
new_root.append(harmonicAngleForce)

# Urey-Bradley Terms 
for ub_element in ureyBradleyForce:
    ub_element.attrib['d'] = "{:15.5f}".format(NM_TO_A * \
                            float(ub_element.attrib['d'])).strip()
    ub_element.attrib['k'] = "{:15.5f}".format(0.5 * KJ_TO_KCAL * (NM_TO_A ** -2) * \
                            float(ub_element.attrib['k'])).strip()
new_root.append(harmonicAngleForce)

# Periodic Torsion Forces
for torsion_element in periodicTorsionForce:
    for key in torsion_element.attrib.keys():
        if 'k' == key[0]:
            torsion_element.attrib[key] = "{:15.5f}".format(KJ_TO_KCAL * \
                                            float(\
                                            torsion_element.attrib[key])).strip()
        elif 'phase' in key[:5]:
            torsion_element.attrib[key] = "{:15.5f}".format(\
                                        float(\
                                        torsion_element.attrib[key])).strip()
new_root.append(periodicTorsionForce)
# Improper torsions
for improper_element in improperTorsionForce:
    if 'Improper' == improper_element.tag:
        improper_element.attrib['k'] = "{:15.5f}".format(0.5 * KJ_TO_KCAL * \
                                        float(improper_element.attrib['k'])).strip()
        improper_element.attrib['theta0'] = "{:15.5f}".format(\
                                            float(\
                                            improper_element.attrib['theta0'])).strip()
new_root.append(improperTorsionForce)

# LJ force terms move into the nonbondedforce terms
for nonbond_element in nonbondedForce:
    # Look through each nonbonded force
    if nonbond_element.tag != "UseAttributeFromResidue":
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
new_tree.write("foyer_charmm.xml", pretty_print=True)
