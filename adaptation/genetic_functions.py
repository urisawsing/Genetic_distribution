import numpy as np

def mutation():
  
#Funció taxa d'adaptacó
def fitness(Ne, s, mu):
  k=(4*Ne*s*mu)/(1-e^(-4*Ne*s))
  return k

def elit_cast(population,n_elit):
  elit_people=[]
  for i in range(n_elit):
    elit_people.append(population[i])
  return elit_people


def cast(population,n_elit):
  casted_people=[]
  p_survive=[]
  for i in range(n_elit,len(population)):
    p_survive[i]=random.random()*population[i][3]
 '''
 continuar aquí
 '''
def cross():
def mutate():

def next_generation(population,n_elit,n_select,n_cross,n_mut):
  temp_population[]
  n_pop=len(population)
  elit_population=elit_cast(population)

  for i in range(n_elit):
    temp_population.append(elit_population[i])

  casted_population=cast(population)

  for i in range(n_select):
    temp_population.append(casted_population[i])

  crossed_population=cross(elit_population,casted_population,n_pop)

  for i in range(n_cross):
    temp_population.append(crossed_population[i])

  temp_population=mutate(temp_population,n_elit)

  return temp_population
  
