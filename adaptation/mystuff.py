import random as rnd
import numpy as np
import math

def fitness(Ne, s, mu):
  k=(4*Ne*s*mu)/(1-math.exp(-4*Ne*s))
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
      individual[j+1]=rnd.randint(0,100)/100
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
    Ne_cross=int((m[0] + f[0])/2)
    s_cross=round((m[1] + f[1])/2,2)
    mu_cross=(m[2] + f[2])/2
    fitness_cross=fitness(Ne_cross, s_cross, mu_cross)
    offspring.append([Ne_cross, s_cross, mu_cross, fitness_cross])

  return offspring
