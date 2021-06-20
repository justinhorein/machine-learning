import numpy as np

input_vector = np.array([1.66, 1.56])
weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

 

