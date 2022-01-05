import numpy as np
import pandas as pd
import random as rnd
import matplotlib.pyplot as plt
import math
import scipy.stats as stats


def saving_data(saved,population,step):
  for i in range(len(saved)):
    saved[i][step]=population[i][3]



def fitness(Ne, s, mu):
  try:
    k=(4*Ne*s*mu)/(1-math.exp(-4*Ne*s))
  except ZeroDivisionError:
    k=0
  return k



def plot_best_fitness(generations,population,fitnesses):
  txt= 'Parameter values of the best solution:'+str(population[0])

  fig = plt.figure()
  ax = plt.axes()
  ax.plot(generations, fitnesses, linestyle='dashdot', color='orangered')
  ax.set(xlabel='Generations', ylabel='Fitness evolution',
         title='Genetic Algorith: optimitzation of the K adaptation value');
  fig.text(.5, .05, txt, ha='center')
  plt.show()


def plot_all_fitness(savings,generations,n_elite,n_offspring):
  #txt= 'Parameter values of the best solution:'+str(population[0])

  fig = plt.figure()
  for i in range(len(savings)):
    if i < n_elite:
      plt.plot(generations, savings[:][i], linestyle='solid', color='orangered',)
    if i > n_elite and i < (n_offspring + n_elite) :
      plt.plot(generations, savings[:][i], linestyle='dotted', color='green',alpha=0.8)
    if i > (n_offspring + n_elite):
      plt.plot(generations, savings[:][i], linestyle='dotted', color='blue',alpha=0.6)
  plt.show()
  '''  
  ax.set(xlabel='Generations', ylabel='Fitness evolution',
         title='Genetic Algorith: optimitzation of the K adaptation value');
  fig.text(.5, .05, txt, ha='center')
  '''

def plot_parameter(generations, fitnesses, best, parameter_track, parameter_name):
  txt= 'Parameter values of the best solution:'+str(best)

  fig, ax1 = plt.subplots()

  color = 'orangered'
  ax1.set_xlabel('Generations')
  ax1.set_ylabel('Fitness evolution', color=color)
  ax1.plot(generations, fitnesses, color=color)
  ax1.tick_params(axis='y', labelcolor=color)

  ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

  color = 'limegreen'
  ax2.set_ylabel(parameter_name, color=color)  # we already handled the x-label with ax1
  ax2.plot(generations, parameter_track, color=color, linestyle='dashdot')
  ax2.tick_params(axis='y', labelcolor=color)

  fig.tight_layout()  # otherwise the right y-label is slightly clipped
  fig.text(.5, .05, txt, ha='center')
  plt.show()


def fitness_sort(n):
  return n[3]


def population_generator(n):
  mu_ne, sigma_ne = 1000, 2000

  mu_s, sigma_s = 0, 0.5
  lower_s, upper_s = (-1-mu_s)/sigma_s, (1-mu_s)/sigma_s

  mu_mu, sigma_mu = 1e-3, 0.005
  lower_mu, upper_mu = (1e-11-mu_mu)/sigma_mu, (0.003-mu_mu)/sigma_mu

  population=[]

  for i in range(n):
    individual=[0,0,0,0]
    for j in range(len(individual)):

      individual[j] = int(abs(np.random.normal(mu_ne,sigma_ne)))

      individual[j+1] = float(abs(stats.truncnorm.rvs(a = lower_s, b = upper_s, 
                                                     loc = mu_s, scale = sigma_s)))
      #individual[j+1] = int(rnd.randint(0,100)/100)

      individual[j+2] = float(abs(stats.truncnorm.rvs(a = lower_mu, b = upper_mu, 
                                                     loc = mu_mu, scale = sigma_mu)))
      #individual[j+2] = abs(np.random.normal(mu_mu, sigma_mut))

      individual[j+3] = fitness(individual[j],individual[j+1],individual[j+2])
      break
    population.append(individual)

  return population

def mutation(population):
  sigma_s = 0.1
  sigma_mu = 0.001

  gamets=[]

  for i in population:
    lower_s, upper_s = (-1-i[1])/sigma_s, (1-i[1])/sigma_s
    lower_mu, upper_mu = (1e-11-i[2])/sigma_mu, (0.003-i[2])/sigma_mu

    Ne_mut = int(abs(np.random.normal(i[0], 50)))

    s_mut = float(abs(stats.truncnorm.rvs(a = lower_s, b = upper_s, 
                                          loc = i[1], scale = sigma_s)))
    #s_mut=round(abs(np.random.normal(i[1], 0.05)),2)

    mu_mut = float(abs(stats.truncnorm.rvs(a = lower_mu, b = upper_mu, 
                                           loc = i[2], scale = sigma_mu)))
    #mu_mut = abs(np.random.normal(i[2], 0.005))

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

    Ne_cross= parents[rnd_indexes[0]][0]
    s_cross= parents[rnd_indexes[1]][1]
    mu_cross= parents[rnd_indexes[2]][2]

    fitness_cross=fitness(Ne_cross, s_cross, mu_cross)
    offspring.append([Ne_cross, s_cross, mu_cross, fitness_cross])

  return offspring

