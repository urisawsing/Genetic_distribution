#Aquí hi hauran les diferents distribucions
import numpy as np

def Gaussian(mu,sig,x):
  return (1/(sig*np.sqrt(2*np.pi)))*np.exp(-((x-mu)**2)/(2*sig**2))
