

import numpy as np
from distributions import *
import pandas as pd
import sys

##############################################
#initial parameters for the Genetic Algorithm#
##############################################
'''
n     :  number of individuals
niter :  number of generations
ndist :  distribution choosing, 1 for Gaussian
n_mut :  mutation ratio
n_elit:  number of elitists
'''

n=50
niter=100
n_mut=0.2
n_elit=5
ndist=1

if ndist==1:
  vec_size=2
else :
  sys.exit("Distribution non available")
  
