import numpy as np

### Define Neural Net ###
def sigmoid(x):
	return 1 / (1 + np.exp(-x))

 
def make_prediction(input_vector, weights, bias):
	layer_1 = np.dot(input_vector, weights) + bias
	layer_2 = sigmoid(layer_1)
	return layer_2

input_vector = np.array([1.66, 1.56])
weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])

### Calculate Prediction 1 ###
prediction = make_prediction(input_vector, weights_1, bias)

print(f"The prediction result is: {prediction}")
# > .7985731

### Calculate Prediction 2 ###
input_vector_2 = np.array([2, 1.5])

prediction2 = make_prediction(input_vector_2, weights_1, bias)

print(f"The prediction 2 result is: {prediction2}")
# > .87101915
print('Prediction 2 is wrong.')

### Calculate Mean Squared Error ###
# MSE: Calculate the difference between the prediction and the target. Square the Result.
target = 0

mse = np.square(prediction2 - target)

print(f"The Mean Squared Error is: {mse}")
# > .7586743596667225

# Calculate Derivative
derivative = 2 * (prediction2 - target)

print(f"The derivative is {derivative}")
# The derivative is: 1.7420383

### Update the weights ###
weights_1 = weights_1 - derivative

print(f"weights_1 = {weights_1}")

### Make New Prediction ###
prediction2 = make_prediction(input_vector_2, weights_1, bias)

error = (prediction2 - target) ** 2

print(f"Prediction: {prediction2};  Error: {error}")



