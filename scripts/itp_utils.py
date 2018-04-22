import numpy as np

import mbuild as mb


#####################
## These are a collecton of python modules
## to operate with gromacs itp files
#####################


def compound_from_itp(itpfile):
    """ Generate mBuild compound from ITP file 

    Parameters
    ---------
    itpfile : str

    Notes
    -----
    Coordinates are neglected
    """
    itplines = open(itpfile,'r').readlines()
    itplines = remove_comments(itplines)

    molecule_name = parse_molecule_name(itplines)

    cmpd = mb.Compound(name=molecule_name)
    cmpd = parse_atoms(itplines, cmpd)
    cmpd = include_bonds(itplines, cmpd)
    cmpd.name = molecule_name

    return cmpd
    


def remove_comments(itplines):
    """ Remove commented lines and tail comments from itplines """
    newlines = []
    for line in itplines:
        if ';' not in line[0] and line.strip():
            newlines.append(line.split(';')[0])

    return newlines

def parse_molecule_name(itplines):
    """ Obtain molecule name """
    moleculetype_directive = find_directive('moleculetype', itplines)
    [molecule_name, nrexcl] = itplines[moleculetype_directive+1].split()

    return molecule_name


def find_directive(directive, itplines):
    """ Find index of directive in itplines """
    for i, line in enumerate(itplines):
        if directive in line and '[' in line and ']' in line:
            return i

    return -1

def parse_atoms(itplines, cmpd):
    """ Return an mBuild compoudn with atoms defined


    Parameters
    ---------
    itplines : 
    cmpd : mb.Compound
    
    Notes
    ------
    nr	type	resnr	residu	atom	cgnr	charge	mass
    """
    atoms_directive = find_directive('atoms', itplines)
    index = atoms_directive

    keep_iterating = True
    while keep_iterating == True:
        index += 1
        atom_info = itplines[index].split()
        if len(atom_info) == 8:
            to_add = mb.Compound(name=atom_info[1])
            cmpd.add(to_add)
        else:
            keep_iterating = False
    return cmpd

def include_bonds(itplines, cmpd):
    """ Add bonds between atoms """

    bonds_directive = find_directive('bonds', itplines)
    index = bonds_directive

    keep_iterating = True
    while keep_iterating == True:
        index += 1
        bond_info = itplines[index].split()
        if '[' not in bond_info[0] and (len(bond_info) == 3 or len(bond_info) == 5):
            cmpd.add_bond([cmpd.children[ int( bond_info[0] ) - 1 ], 
                           cmpd.children[ int( bond_info[1] ) - 1 ]])
        else:
            keep_iterating = False
    return cmpd

def coordinates_from_compound(source, sink):
    """ Pull coordinates from source into sink
   
    Parameters
    ----------
    source : mb.Compound()
    sink : mb.Compound()

    
    """
    source_particles = [p for p in source.particles()]
    sink_particles = [p for p in sink.particles()]
    assert len(source_particles) == len(sink_particles), \
        "Number particles do not match"
    for i, j in zip(source_particles, sink_particles):
        j.xyz = i.xyz

    return sink

def coordinates_from_file(source, sink):
    """ Pull coordinates from source into sink

    Parameters
    ---------
    source : str
        file of source structure
    sink : mb.Compound()
    """
    return coordinates_from_compound(mb.load(source), sink)

def read_section(directive, itplines):
    all_lines = []
    i = find_directive(directive, itplines)
    keep_iterating = True
    while keep_iterating:
        i += 1
        if itplines[i].strip():
            to_add = itplines[i].strip().split(';')[0]
            if to_add and '[' not in to_add and ']' not in to_add:
                all_lines.append(to_add)
            else:
                keep_iterating = False
        else:
            keep_iterating = False
    return all_lines
