

import numpy as np
from distributions import *
import pandas as pd
import sys

##############################################
#initial parameters for the Genetic Algorithm#
##############################################
'''
n       :  number of individuals
niter   :  number of generations
ndist   :  distribution choosing, 1 for Gaussian
n_mut   :  mutation ratio
n_elit  :  number of elitists
n_cross :  number of individuals which will have crossover
n_select:  number of individuals
'''

n=50
niter=100
n_mut=0.2
n_elit=5
n_cross=20
n_select=10
ndist=1


# if any other distribution is added,
if ndist==1:
  vec_size=2
else :
  sys.exit("Distribution non available")
 

#generation of the initial population
population=[]
for i in range(n):
  individual=[]
  for j in range(vec_size):
    individual[j]=dsitributions.generate(ndist,j)
  population.append(individual)

  







  
 
  
