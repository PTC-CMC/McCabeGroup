# How to use
After pip-installing from the `McCabeGroup` directory,
access to the `atomistic` module and all molecular prototypes 
should immediately be available,

```
>>> import mccabe_group
>>> mccabe_group.atomistic.dspc.DSPC()
/Users/ayang41/Programs/mdtraj/mdtraj/formats/mol2.py:215: FutureWarning: read_table is deprecated, use read_csv instead.
  index_col=0, header=None, sep="\s+", engine='python')
<DSPC 142 particles, non-periodic, 141 bonds, id: 4309479264>
```

# Folders
Molecular prototypes that specify coordinates, masses, bonds, angles, charges, and atomtypes  
By default, these parameters and prototypes are based on CHARMM36 and Guo, Moore, 
Iacovella, and McCabe's ceramide additions (2013 JCTC)  
Default units: Mass (amu), distance (Angstrom), charge (e)  
Txt files + `txt_to_xml.py` -> XML Prototype file  
XML Prototype file + `xml_to_cmpd.py` -> mbuild Compound python module and properly-aligned mol2 structure (with bonds)  
In general, molecules are aligned such that headgroups are centered on the origin with the tails oriented in negative
Z space 
## Itp files and Charmm36 FF
The FFA and ceramides were based on Tim's itps, which pulled from the prototype.txt 
files. As such, all bonded parameters are explicitly stated in each molecule.itp, and
parameters do not need to be pulled from ffbonded.itp and ffnonbonded.itp.  
DPPC and DSPC were based off `Charmm-GUI`. While bonds, angles, dihedrals, and 1,4 pairs
are specified within the itp files, the parameters are not. 
As such, the bonded and nonbonded 
parameters are pulled from ffbonded.itp and ffnonbonded.itp  
The FFXML was generated using parmed to converted forcefield.itp, and then adding some parameters that were omitted.
## 1,4 pairs and interactions  
There is no general rule for 1,4 scaling of nonbonded interactions. Instead, certain
1,4 pairs are given particular sigma and epsilon parameters.  
The FFA and ceramides do not appear to have any special 1,4 interactions. As such,
`nrexcl=2`, and 1,4 pairs are just treated like any other nonbonded interaction. As of
[PR#27](https://github.com/PTC-CMC/McCabeGroup/pull/27), `nrexcl=3` and 1,4 pairs are enumerated in order to make these gromacs files
compatible with `ParmEd` (and subsequently, `OpenMM`).
The DSPC and DPPC molecules have special 1,4 interactions. As such, nrexcl=3, and 
1,4 pairs are enumerated within the itp files, with parameters pulled from
ffnonbonded.itp  
In lammps special bonds should be set to 0 because 1,4 interactions are handled 
in the dihedral routines (charmm style dihedrals). The weights in the charmm dihedrals
correspond to scaling the 1,4 nonbonded interactions. For example, if the same dihedral
is parameterized with 4 dihedral terms (4 sets of coefficients), then the 
nonbonded force for that 1,4 pair is computed 4 times. In order to compensate for this
repetitive calculation, the weight must be 0.25.
## Compatibility with Foyer
In this repo is the `foyer_charmm.xml`. 
In this foyer XML, SMARTS definitions utilize the coarse-grain convention,
where the SMARTS definitions are just the names of the particles prefaced with an underscore.
In this design, the SMARTS definitions and particle names should correspond to the actual atom types for ease in debugging and comparison to other simulation workflows.
For example, a choline nitrogen should have the particle name `_NTL` with the SMARTS definition being `[_NTL]`, as this choline nitrogen has the `NTL` atom type.

When using these mbuild Compounds, you can generally pass the flag
`use_atom_name=True` which will use the atomic name for each particle's name,
OR you can pass `use_atom_name=False` which will use the atom type for each particle's name.
We desire the latter, where the particle names correspond to the atom type.
This may throw gromacs warnings where the atom names in the GRO file do not match the atom names in the TOP file, but that's largely cosmetic and insignificant; atom names and atom types really only matter in the TOP file and the GRO file is just for the user.

When passing `use_atom_name=False` to the constructor's for each mbuild Compound, they WILL NOT have the underscore prefaced.
This is largely a cosmetic choice and helpful for debugging/visualization in notebooks.
Prior to any atom-typing in foyer, you will need to prepend the underscore to each particle:

```
# Prepending underscore
for p in my_compound.particles():
    p.name = "_" + p.name

# Converting to parmed.Structure with residue names
structure = my_compound.to_parmed(residues=['DSPC', 'ecer2'])

# Applying the forcefield
parametrized_structure = ff.apply(structure, assert_dihedral_params=False)
```
