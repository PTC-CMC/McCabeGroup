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
DPPC and DSPC were based off Charmm-GUI. While bonds, angles, dihedrals, and 1,4 pairs
are specified within the itp files, the parameters are not. 
As such, the bonded and nonbonded 
parameters are pulled from ffbonded.itp and ffnonbonded.itp  
## 1,4 pairs and interactions
There is no general rule for 1,4 scaling of nonbonded interactions. Instead, certain
1,4 pairs are given particular sigma and epsilon parameters.  
The FFA and ceramides do not appear to have any special 1,4 interactions. As such,
nrexcl=2, and 1,4 pairs are just treated like any other nonbonded interaction.  
The DSPC and DPPC molecules have special 1,4 interactions. As such, nrexcl=3, and 
1,4 pairs are enumerated within the itp files, with parameters pulled from
ffnonbonded.itp
