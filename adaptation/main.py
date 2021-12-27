import numpy as np
import genetic_functions as genetic
import pandas as pd
import sys

##############################################
#initial parameters for the Genetic Algorithm#
##############################################
'''
n       :  number of individuals
niter   :  number of generations
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



#generation of the initial population
mu_ne, sigma_ne = 1000, 1000
mu_mut, sigma_mut = 1e-3, 0.01
n=10

population=[]
for i in range(n):
  individual=[0,0,0,0]
  for j in range(len(individual)):
  	individual[j]=int(abs(np.random.normal(mu_ne,sigma_ne)))
  	individual[j+1]=rnd.randint(0,100)/100
  	individual[j+2]=abs(np.random.normal(mu_mut, sigma_mut))
  	individual[j+3]=fitness(individual[j],individual[j+1],individual[j+2])
  	break
  population.append(individual)

fitnesses=np.zeros(n)

def fitness_sort(ind):
	return ind[3]

for i in population:
	population.sort(reverse=True, key=fitness_sort)
  
#begin iterations 

while (iter<niter):
  
  #calculate fitness
  
  for i in range(n):
    if fitnesses[i]<=0:
      fitnesses[i]=genetic.fitness(population[i])
    else:  
      
  #calculate next generation
  
  temp_population,best_ind = next_generation(population,n_elit, n_select, n_cross, n_mut)
  
  #print every some steps which is the best fitness
  if iter % (niter/10) == 0 :
    print("Generation", iter, "with a best fitness equals to", best_ind[0])
   
  #writing the new population into the old variable
  population = temp_population
  #updating iteration
  iter=iter+1
  
print("Exited Genetic algorithm")
print("Best individual with fitness",best_ind[0],"and parameters",best_ind)
  
  
