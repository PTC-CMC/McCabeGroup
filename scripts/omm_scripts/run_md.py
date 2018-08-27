import sys
import parmed as pmd
import simtk.openmm as mm
import simtk.openmm.app as app
import simtk.unit as u

#######################
### Somewhat common OpenMM script for use with the CHARMM force field
### Note the use of parmed to generate the mm.Structure (though this could 
### be easily interchanged with the use of foyer)
### Note the system parameters and barostat parameters
#######################

topfile = 'compound.top'
grofile = 'npt.gro'
temp = 305 * u.kelvin
pressure = 1 * u.bar
timestep = 2.0 * u.femtoseconds
sim_time = 100 * u.nanoseconds
platform = mm.Platform.getPlatformByName('OpenCL')
properties = {'DeviceIndex': 0}
n_steps = int(round(sim_time/timestep))

print("Reading grofiles")
top = pmd.load_file(topfile, xyz=grofile)

print("Creating system from topology")
system = top.createSystem(nonbondedMethod=app.PME,
                            constraints=app.HBonds,
                            nonbondedCutoff=12.0*u.angstroms,
                            switchDistance=10.0*u.angstroms)
barostat = mm.MonteCarloMembraneBarostat(pressure, 0.0*u.bar*u.nanometer, 
                                      temp,
                                      mm.MonteCarloMembraneBarostat.XYIsotropic,
                                      mm.MonteCarloMembraneBarostat.ZFree,
                                      100)
system.addForce(barostat)
print("Creating integrator")
integrator = mm.LangevinIntegrator(temp, 
                                    1.0/u.picoseconds, 
                                    timestep)

print("Creating Simulation")
sim = app.Simulation(top.topology, system, integrator, platform, properties)

print("Setting context")
sim.context.setPositions(top.positions)
sim.reporters.append(app.StateDataReporter(open('thermo.log','a'), 1000, step=True, time=True,
                                            potentialEnergy=True,
                                            temperature=True,
                                            volume=True, speed=True))
sim.reporters.append(app.DCDReporter('trajectory.dcd', 2500))
# Uncomment the following line only if trajectory.dcd exists and you want to append
#sim.reporters.append(app.DCDReporter('trajectory.dcd', 2500, append=True))
sim.reporters.append(app.CheckpointReporter('trajectory.chk', 2500))
# Load the checkpoint
#with open('my_checkpoint.chk', 'rb') as f:
#        sim.context.loadCheckpoint(f.read())
print("Running MD")
remaining_time = sim_time - sim.context.getState(-1).getTime()
remaining_steps = int(round(remaining_time/timestep))

sim.step(remaining_steps)

pdbreporter = app.PDBReporter('trajectory.pdb', 5000)
pdbreporter.report(sim, sim.context.getState(-1))
