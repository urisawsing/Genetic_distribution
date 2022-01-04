import numpy as np
import pandas as pd
import random as rnd
import math


def fitness(Ne, s, mu):
  try:
    k=(4*Ne*s*mu)/(1-math.exp(-4*Ne*s))
  except ZeroDivisionError:
    k=0
  return k


def fitness_sort(n):
  return n[3]


def population_generator(n):
  mu_ne, sigma_ne = 1000, 1000
  mu_mut, sigma_mut = 1e-3, 0.01

  population=[]

  for i in range(n):
    individual=[0,0,0,0]
    for j in range(len(individual)):
      individual[j]=int(abs(np.random.normal(mu_ne,sigma_ne)))
      individual[j+1]=rnd.randint(0,90)/100
      individual[j+2]=abs(np.random.normal(mu_mut, sigma_mut))
      individual[j+3]=fitness(individual[j],individual[j+1],individual[j+2])
      break
    population.append(individual)

  return population


def mutation(population):
  
  gamets=[]

  for i in population:
    Ne_mut=int(abs(np.random.normal(i[0], 10)))
    s_mut=round(abs(np.random.normal(i[1], 0.01)),2)
    mu_mut=abs(np.random.normal(i[2], 0.001))
    gamets.append([Ne_mut, s_mut, mu_mut])

  return gamets


def crossover(prog_1, prog_2):

  offspring=[]

  for i,m in enumerate(prog_1):
    f=prog_2[i]
    rnd_indexes=np.random.randint(2, size=3)

    parents=[]
    parents.append(m)
    parents.append(f)

    Ne_cross= parents[int(rnd_indexes[0])][0]
    s_cross= parents[rnd_indexes[1]][1]
    mu_cross= parents[rnd_indexes[2]][2]

    fitness_cross=fitness(Ne_cross, s_cross, mu_cross)
    offspring.append([Ne_cross, s_cross, mu_cross, fitness_cross])

  return offspring
