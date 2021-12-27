#Aquí hi hauran les diferents distribucions
import numpy as np

def Gaussian(mu,sig,x):
  return (1/(sig*np.sqrt(2*np.pi)))*np.exp(-((x-mu)**2)/(2*sig**2))



def generate(ndist,element):
  individual=[]
  if ndist == 1:
    individual = gauss_gen(element)
  else:
    print("non correct individual")
    
  
    
