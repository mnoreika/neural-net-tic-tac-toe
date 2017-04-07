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

		for bias, weight in zip(self.biases, self.weights):
			layer_outputs = self.activation_function(numpy.dot(weight, layer_outputs))
			O.append(layer_outputs)

		return O


	def back_propagate(self, training_data):	

		for inputed, expected in training_data:
			for epoch in range(1000):
				O = net.feedforward(inputed)
				one_vector = [1] * len(O)
				
				# Input layer has no outputs
				last_layer = self.number_of_layers - 2

				# Updating weights of the output layer
				delta_error_L = numpy.multiply(numpy.multiply(O[last_layer], 1 - O[last_layer]), O[last_layer] - expected)


				for i in range(len(self.weights[last_layer]) - 1, -1, -1):
					delta_weight = numpy.multiply(-1 * self.learning_rate,  numpy.multiply(delta_error_L[i], O[last_layer - 1]))
					
					for j in range(len(self.weights[last_layer][i])):
						self.weights[last_layer][i][j] += delta_weight[j]
				
				
				# Updating weights of the hidden layers
				previous_delta_error = delta_error_L

				for i in range(last_layer - 1, -1, -1):
					delta_error_l = []

					for j in range(len(self.weights[i])):
						sum_of_L = 0 
						print (i)
						for k in range(len(self.weights[i + 1])):
							sum_of_L += previous_delta_error[k] * self.weights[i + 1][k][j]


						delta_error_l_neuron = O[i][j] * (1 - O[i][j]) * sum_of_L
						delta_error_l.append(delta_error_l_neuron)

						delta_weight = numpy.multiply(-1 * self.learning_rate,  numpy.multiply(delta_error_l_neuron, O[i - 1]))
						print(delta_weight)
						# Updating the weights of a particular neuron
						for w in range(len(self.weights[i][j])):
							self.weights[i][j][w] += delta_weight[w]


						
					previous_delta_error = delta_error_l

				# break	
					# print (previous_delta_error)
					# print (weights[i])
				# sum_of_L = 0 
				# for k in range(len(previous_delta_error)):
				# 	sum_of_L += numpy.dot(previous_delta_error[k], self.weights[i])


			    # delta_error_l = numpy.multiply(numpy.multiply(O[i], 1 - O[i]), sum_of_L)
			    # print (previous_delta_error_transposed)



				# previous_delta_error = delta_error_l

				# print (delta_error_l)


				# for j in range(len(self.weights[i])):
				# 	print()
				# 	print (delta_error_l[j])
				# 	print(O[last_layer - 2 - i])

				# 	delta_weight = numpy.multiply(-1 * self.learning_rate,  numpy.multiply(delta_error_l[i][j], O[last_layer - 2 - i]))

				# 	print (delta_weight)	
					
				# 	# Calculating the delta
				# 	for n in range(len(self.weights[i][j])):
						

				# 		print (delta_weight)	

				# 		for w in range(len(self.weights[i][j])):
				# 			print (self.weights[i][j][n])

				# 		self.weights[i][j][w] += delta_weight[w]
				# 		print (self.weights[i][j][w])
				

				

					
				
			



net = Network([3, 9, 1, 3])

# inputs = [2, 3]		


# # net.feedforward(inputs)
net.back_propagate([([0, 0, 0], [0.5, 0.5, 0.5])]);

result = net.feedforward([0, 0, 0])

print (result)
# # net.learn([(5, 0)])
