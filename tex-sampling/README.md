#tex-sampling
This repository provides basic functions to implement the Random-Walk Molecular Dynamics (RWMD) methodology.
Briefly, RWMD is a random-walk through temperature space, similar to parallel tempering techniques.
After an interval number of steps, a Monte Carlo step is attempted to change the simulation temperature to an adjacent temperature window. If the proposed temperature has been visited less frequently, it is accepted. If not, a random number [0, 1) is computed and compared to `exp(frequencies[current_T] - frequencies[attempt_T])`. If the random number is less than this quantity, accept the move. If not, keep the current temperature for the next interval.

## How to use
This code provides the bare-bone algorithm for choosing temperatures and storing them into a dictionary of temperatures and frequencies (`pyrex.py`). Incorporate this package into your own workflows and simulation engines as necessary.

This methodology is outlined in 
Moore, T. C., Hartkamp, R., Iacovella, C. R., Bunge, A. L., & McCabe, C. (2018). Effect of Ceramide Tail Length on the Structure of Model Stratum Corneum Lipid Bilayers. Biophysical Journal, 114(1), 113–125. https://doi.org/10.1016/j.bpj.2017.10.031
```
@article{Moore2018,
author = {Moore, Timothy C. and Hartkamp, Remco and Iacovella, Christopher R. and Bunge, Annette L. and McCabe, Clare},
doi = {10.1016/j.bpj.2017.10.031},
file = {:Users/ayang41/Research/Library/Moore2018Effect.pdf:pdf},
issn = {00063495},
journal = {Biophysical Journal},
number = {1},
pages = {113--125},
publisher = {Biophysical Society},
title = {{Effect of Ceramide Tail Length on the Structure of Model Stratum Corneum Lipid Bilayers}},
url = {http://linkinghub.elsevier.com/retrieve/pii/S0006349517311542},
volume = {114},
year = {2018}
}
```
