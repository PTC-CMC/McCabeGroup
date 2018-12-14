# ISIS molecule (isostearyl isostearate)
* Used smiles + Charmm-gui to get ITP and coordinates, but coordinates were a 
sort of splayed configuration
* Used a bit of `rotate_isis.py` to try to align both tails in the same direction
* Then run EM on it
* Then use the other bit of `rotate_isis.py` to put head group at origin and
rest of tail in negative Z
