import numpy as np
import random as rnd
import functions as ms
from matplotlib import pyplot as plt

##################################
#  Genetic Algorithm in 7 steps  #
##################################

'''
Parameters
    -----------------------------------------------------------------
    N:          integer
                population size
    n_elite:    integer
                selected individuals to mantain in the new population
        !! mus be pair
    n_progenie: integer
                number of selected indivudals to cross
    n_bros:     integer
                number of siblings to generate in each crossover
    n_gen:      integer
                generations to be run
    -----------------------------------------------------------------
'''
#Parameters
N=50
n_elite=5
n_progenie=20
n_bros=2
n_gen=10000

#Track
count=0
savings=np.zeros((N,n_gen))
generations=[]
fitnesses=[]
Ne_track=[]
s_track=[]
mu_track=[]

#1. Setting the original population
population=ms.population_generator(N)
for i in population:
  population.sort(reverse=True, key=ms.fitness_sort)

while count<n_gen:
    
    #2. Selecting best individuals, the elite and the progeny
    elite=population[0:n_elite]
    progenie=population[n_elite:int(n_elite+n_progenie)]

    #3. Generating the mutated gamets from the progeny
    gamets=ms.mutation(progenie)

    #4. Defining the breeding pattern
    prog_1=gamets[0:int(n_progenie/2)]
    prog_2=gamets[int(n_progenie/2):int(n_progenie+1)]

    #5. Crossover of the gamets as times as the number of siblings specified
    offspring=[]
    for i in range(n_bros):
      birth=ms.crossover(prog_1, prog_2)
      offspring.append(birth)
    offspring=sum(offspring, [])

    #6. Adding variation by migration from a new random generated population
    n_migrants=int(N-n_elite-(n_progenie/2)*n_bros)
    migrants=ms.population_generator(n_migrants)

    #7. Setting the new population
    new_population=[*elite, *offspring, *migrants]
    for i in new_population:
      new_population.sort(reverse=True, key=ms.fitness_sort)

    generations.append(count)
    Ne_track.append(new_population[0][0])
    s_track.append(new_population[0][1])
    mu_track.append(new_population[0][2])
    fitnesses.append(new_population[0][3])

    ms.saving_data(savings,population,count)

    population=new_population

    count=count+1
 
#Visualise the performance
ms.plot_best_fitness(generations,population,fitnesses)
#print(savings)
ms.plot_all_fitness(savings,generations,n_elite,n_progenie)
    



