import numpy as np 
def init_weights(shape):
    return np.random.normal(loc=0.0, scale=0.1, size=shape) 
def init_bias(shape):
    return np.zeros(shape)