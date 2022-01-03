import numpy as np
import random as rnd
import mystuff as ms

##################################
#  Genetic Algorithm in 7 steps  #
##################################

'''
Parameters
    ----------
    N:      integer
            population size
    elite:  integer
            selected individuals to cross
        !! mus be pair
    bros:   integer
            number of siblings to generate in each crossover
    ----------
'''

N=50
elite=10
bros=2

#1. Setting the original population
population=ms.population_generator(N)
for i in population:
  population.sort(reverse=True, key=ms.fitness_sort)
  
#2. Selecting best individuals, from now on, the progeny
selected=population[:sel]

#3. Generating the mutated gamets from the progeny
gamets=ms.mutation(selected)

#4. Defining the breeding pattern
prog_1=gamets[0:sel/2]
prog_2=gamets[sel:(sel/2)+1]

#5. Crossover of the gamets as times as the number of siblings specified
offspring=[]
for i in range(bros):
  birth=crossover(prog_1, prog_2)
  offspring.append(birth)

#6. Adding variation by migration from a new random generated population
migrants=ms.population_generator(N-2*sel)

#7. Setting the new population
new_population=offspring+migrants
for i in new_population:
  new_population.sort(reverse=True, key=ms.fitness_sort)

for i in new_population:
  print(i)
print('\n')
