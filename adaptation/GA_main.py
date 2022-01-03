import numpy as np
import random as rnd

#######################
#  Genetic Algorithm  #
#######################
'''
Parameters
    ----------
    N:  integer
        population size
    sel:integer
        selected individuals to cross
        !! mus be pair
    ----------
'''

N=50
sel=10

#1. Setting the original population
population=population_generator(N)
for i in population:
  population.sort(reverse=True, key=fitness_sort)
  
#2. Selecting best individuals seted by now as progeny
selected=population[:sel]

#3. Applying mutation to the gamets of the selected progeny
gamets=mutation(selected)

#4. Defining the breeding pattern
prog_1=gamets[0:sel/2]
prog_2=gamets[sel:(sel/2)+1]

#5. Crossover of the gamets generating two siblings
offspring_1=crossover(prog_1, prog_2)
offspring_2=crossover(prog_1, prog_2)

#6. Adding variation by migration (new random generated population)
migrants=population_generator(N-2*sel)

#7. Setting the new population
new_population=offspring_1+offspring_2+migrants
for i in new_population:
  new_population.sort(reverse=True, key=fitness_sort)

for i in new_population:
  print(i)
print('\n')
