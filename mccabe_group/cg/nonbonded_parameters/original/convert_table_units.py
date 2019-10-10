import numpy as np
import glob
import os

#############################
## This script is used to convert the original tabulated potentials
## into other unit systems
## Distance = 6 Angstroms
## Energy = 0.1 kcal/mol
## Force = Energy/Distance
#############################
TABLE_ENERGY_TO_KCAL = 0.1
TABLE_DISTANCE_TO_A = 6
TABLE_FORCE_TO_KCAL_A = TABLE_ENERGY_TO_KCAL / TABLE_DISTANCE_TO_A

KCAL_TO_KJ = 4.184
A_TO_NM = 0.1

TABLE_ENERGY_TO_KJ = TABLE_ENERGY_TO_KCAL * KCAL_TO_KJ
TABLE_DISTANCE_TO_NM = TABLE_DISTANCE_TO_A * A_TO_NM
TABLE_FORCE_TO_KJ_NM = TABLE_ENERGY_TO_KJ / TABLE_DISTANCE_TO_NM




tabulated_potentials = glob.glob('*.txt')
input_dir = os.getcwd()
output_dir = os.path.join(input_dir, "..", 'gmx')
for table_file in tabulated_potentials:
    tabulated_potential = np.loadtxt(table_file)
    tabulated_potential[:,0] *= TABLE_DISTANCE_TO_NM
    tabulated_potential[:,1] *= TABLE_ENERGY_TO_KJ
    tabulated_potential[:,2] *= TABLE_FORCE_TO_KJ_NM
    np.savetxt(os.path.join(output_dir, table_file), tabulated_potential)

#tabulated_potentials = glob.glob('*.txt')
#input_dir = os.getcwd()
#output_dir = os.path.join(input_dir, "..", 'real')
#for table_file in tabulated_potentials:
#    tabulated_potential = np.loadtxt(table_file)
#    tabulated_potential[:,0] *= TABLE_DISTANCE_TO_A
#    tabulated_potential[:,1] *= TABLE_ENERGY_TO_KCAL
#    tabulated_potential[:,2] *= TABLE_FORCE_TO_KCAL_A
#    np.savetxt(os.path.join(output_dir, table_file), tabulated_potential)
#
