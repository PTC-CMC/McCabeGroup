from parmed import load_file
from parmed.gromacs.gromacstop import GromacsTopologyFile
from parmed.openmm.parameters import OpenMMParameterSet

itp = GromacsTopologyFile('forcefield.itp')
#itp = GromacsTopologyFile('ffa12.top')
omm_pset = OpenMMParameterSet.from_parameterset(itp.parameterset)
omm_pset.write('forcefield_frompmd_raw.xml')
