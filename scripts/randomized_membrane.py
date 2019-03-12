import unyt as u
import numpy as np

import mbuild as mb


class Randomized_Membrane(mb.Compound):
    def __init__(leaflet_info, 
            APL=0.52 * u.nm**2, lipid_density=1.12 * u.Unit('g/(cm**3)'),
            n_lipid_leaflet=64, n_solvent_per_lipid=10,
            solvent_density=0.9 * u.Unit('g/(cm**3)'), solvent_mass=72 * u.Unit('amu')):
        """ Initialize randomized lipids in solvent

        Parameters
        ---------
        leaflet_info : n x 2 tuple
            First column, mb.Compound
            Second column, # of lipids in a leaflet (int)
        APL: Area per lipid (Unyt.unit)
        lipid_density : density of lipids (Unyt.unit)
        n_lipid_leaflet : number of lipids per leaflet (int)
        n_solvent_per_lipid : number of solvent molecules per lipid (int)
        solvent_density : density of solvent (Unyt.unit)
        solvent_mass : mass of solvent molecule (Unyt.unit)

        Returns
        ------
        System : mb.Compound
            One layer of water, middle layer of randomized lipids, 
            another layer of water

        Notes
        -----
        System is initialized with center at origin, but everything eventually
        gets translated/written with bottomleft origin
        """

        super(Randomized_Membrane, self).__init__()

        # Leaflet/membrane properties
        n_lipid_leaflet = sum([val for _, val in leaflet_info])
        leaflet_volume = 0
        for molecule, n in leaflet_info:
            mass = n * np.sum([72 for _ in molecule.particles()]) * u.Unit('amu') 
            leaflet_volume += mass/lipid_density
        total_area = APL * n_lipid_leaflet
        leaflet_height = leaflet_volume / total_area
        lx = total_area ** 0.5
        lx.convert_to_units(u.nm)
        ly = total_area ** 0.5
        ly.convert_to_units(u.nm)
        lz = 2 * leaflet_height
        lz.convert_to_units(u.nm)
        
        # Solvent things
        n_solvent = n_solvent_per_lipid * n_lipid_leaflet
        total_solvent_mass = n_solvent * solvent_mass 
        solvent_volume = total_solvent_mass / solvent_density
        solvent_height = solvent_volume / total_area
        solvent_height.convert_to_units(u.nm)
        
        lipid_box = mb.Box(mins=[-lx/2, -ly/2, -lz/2], 
                            maxs=[lx/2, ly/2, lz/2])
        lower_solvent_box = mb.Box(mins=[-lx/2, -ly/2, -lz/2 - solvent_height],
                                    maxs=[lx/2, ly/2, -lz/2])
        upper_solvent_box = mb.Box(mins=[-lx/2, -ly/2, lz/2],
                                    maxs=[lx/2, ly/2, lz/2 + solvent_height])
        
        
        # Do packing for each box
        filled_lipid_box = mb.fill_box([cmpd for cmpd, _ in leaflet_info], 
                    n_compounds=[2*val for _, val in leaflet_info], 
                    box=lipid_box, overlap=0.05)
        filled_lower_solvent = mb.fill_box(mb.Particle(name="_W"), 
                n_compounds=n_solvent,
                box=lower_solvent_box, overlap=0.05)
        filled_upper_solvent = mb.fill_box(mb.Particle(name="_W"), 
                n_compounds=n_solvent,
                box=upper_solvent_box, overlap=0.05)
        self.add(
                [filled_lipid_box, filled_lower_solvent, filled_upper_solvent])
        self.translate([
            -1 * np.min(system.xyz[:,0]),
            -1 * np.min(system.xyz[:,1]),
            -1 * np.min(system.xyz[:,2])
            ])

