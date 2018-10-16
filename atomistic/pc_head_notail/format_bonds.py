import numpy as np
import mbuild as mb
import pdb

bonds = open('bonds.txt', 'r').readlines()
for entry in bonds:
    print("{:<6}{:>5}{:>5}".format("CONECT", entry.split()[1], entry.split()[2]))
