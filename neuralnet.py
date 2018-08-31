#!/usr/bin/env python3
import numpy as np

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NeuralNetwork():
    def __init__(self, x, y):
        np.random.seed(1)
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1],4)
        self.weights2 = np.random.rand(4,1)
        self.y = y
        self.output = np.zeros(y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) *
            sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2*(self.y - self.output) *
            sigmoid_derivative(self.output),self.weights2.T) *
            sigmoid_derivative(self.layer1)))

        self.weights1 += d_weights1
        self.weights2 += d_weights2


test_data = np.array([[2,2],
                    [2,3],
                    [10,10],
                    [21,11],
                    [5,6],
                    [7,7],
                    [12,12],
                    [2,12]])

test_outputs = np.array([[1],
                        [1],
                        [0],
                        [0],
                        [1],
                        [1],
                        [1],
                        [1]])

nn = NeuralNetwork(test_data,test_outputs)

for i in range(50000):
    nn.feedforward()
    nn.backprop()

print(nn.output)
