import random

import numpy

class Network():
	# numpy.random.randn(y, x)
	def __init__(self, layer_sizes):
		self.number_of_layers = len(layer_sizes)
		self.layer_sizes = layer_sizes
		self.biases = [numpy.random.randn(y, 1) for y in layer_sizes[1:]]
		self.weights = [numpy.random.randn(y, x) for x, y in zip(layer_sizes[:-1], layer_sizes[1:])]
		self.activation_function = self.sigmoid
		self.learning_rate = 0.2


	def sigmoid(self, vector):
		return 1.0 / (1.0 + numpy.exp(-vector))

	def feedforward(self, inputs):
		O = []
		layer_outputs = inputs

		for biases, weights in zip(self.biases, self.weights):
		
			weighted_sum = numpy.dot(weights, layer_outputs)
			z = []

			for i in range(len(weighted_sum)):
				print (biases[i][0])
				z.append(weighted_sum[i] + biases[i][0]) 

			layer_outputs = self.activation_function(numpy.array(z))
			# print (len(layer_outputs))
			# print (layer_outputs)
			# print ()
			O.append(layer_outputs)

			outputs = []
			# for i in range(len(weights)):
			# 	output = 0
			# 	for j in range(len(weights[i])):
			# 		output += weights[i][j] * layer_outputs[i]

			# 	outputs.append(output)
			# 	print (output)	

			# print (outputs)	
			# layer_outputs = outputs
			# O.append(outputs)
			

		return O


	def back_propagate(self, training_data):	

		for epoch in range(1000):
			for inputed, expected in training_data:
				
					O = net.feedforward(inputed)
					one_vector = [1] * len(O)
					
					# Input layer has no outputs
					last_layer = self.number_of_layers - 2

					# Updating weights of the output layer
				
					delta_error_L = numpy.multiply(numpy.multiply(O[last_layer], 1 - O[last_layer]), O[last_layer] - expected)


					for i in range(len(self.weights[last_layer]) - 1, -1, -1):
						delta_weight = numpy.multiply(-1 * self.learning_rate,  numpy.multiply(delta_error_L[i], O[last_layer - 1]))
						delta_bias = -1 * self.learning_rate * delta_error_L[i]

						print ("DELTA_SIGMA ", delta_bias)

						for j in range(len(self.weights[last_layer][i])):
							self.weights[last_layer][i][j] += delta_weight[j]

						# Updating the bias 
						self.biases[last_layer][i] += delta_bias
					
					
					# Updating weights of the hidden layers
					previous_delta_error = delta_error_L

					for i in range(last_layer - 1, -1, -1):
						delta_error_l = []

						for j in range(len(self.weights[i])):
							sum_of_L = 0 
							
							for k in range(len(self.weights[i + 1])):
								sum_of_L += previous_delta_error[k] * self.weights[i + 1][k][j]


							delta_error_l_neuron = O[i][j] * (1 - O[i][j]) * sum_of_L
							delta_error_l.append(delta_error_l_neuron)

							delta_weight = numpy.multiply(-1 * self.learning_rate,  numpy.multiply(delta_error_l_neuron, O[i - 1]))

							delta_bias = -1 * self.learning_rate * delta_error_l_neuron
							
							# print(delta_weight)
							# Updating the weights of a particular neuron
							for w in range(len(self.weights[i][j])):
								self.weights[i][j][w] += delta_weight[w]

							# Updating the bias 	
							self.biases[i][j] += delta_bias	


							
						previous_delta_error = delta_error_l
					

					
				
			



net = Network([9, 9, 9, 9])

# inputs = [2, 3]		


# # net.feedforward(inputs)
net.back_propagate([([0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1]), ([1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0])]);


result = net.feedforward([1, 1, 1, 1, 1, 1, 1, 1, 1])
print ("Result 1: ", result[net.number_of_layers - 2])
result = net.feedforward([0, 0, 0, 0, 0, 0, 0, 0, 0])
print("Result 2: ", result[net.number_of_layers - 2])


# print (result[net.number_of_layers - 2])
# net.learn([(5, 0)])
