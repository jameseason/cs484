# James Eason

import numpy as np
import random

def initialize_weights(hidden_nodes):
    np.random.seed(1)
    return 2*np.random.random(hidden_nodes) - 1

def sigmoid(x):
	return 1/(1+np.exp(-x))

hidden_nodes = 2 #5
weight0 = initialize_weights(hidden_nodes) #weights between input and hidden
weight1 = initialize_weights(hidden_nodes) #weights between hidden and output
training_examples = [(-1, 2), (-0.9, 1.81), (-0.8, 1.64), 
    (-0.7, 1.49), (-0.6, 1.36), (-0.5, 1.25), (-0.4, 1.16),
    (-0.3, 1.09), (-0.2, 1.04), (-0.1, 1.01), (0, 1), 
    (0.1, 1.01), (0.2, 1.04), (0.3, 1.09), (0.4, 1.16),
    (0.5, 1.25), (0.6, 1.36), (0.7, 1.49), (0.8, 1.64),
    (0.9, 1.81), (1, 2)]

for z in range(0, 2501):
    random.shuffle(training_examples)
    totalerror = 0
    for ex in training_examples:
        # Calculate hidden and output layers using weights
        in_layer = ex[0]
        hidden_layer = []
        for w in weight0:
            hidden_layer.append(sigmoid(in_layer * w))
        out_layer = 0
        for x in range(0, len(weight1)):
            out_layer += hidden_layer[x]*weight1[x]
        
        # Calculate error
        prediction = sigmoid(out_layer) 
        actual = ex[1]
        error = 0.5 * (actual - prediction)**2
        totalerror += error
        
        # Local error
        for x in range(0, len(weight1)):
            #Output layer
            out1 = -(actual - prediction)
            out2 = prediction * (1 - prediction)
            out3 = hidden_layer[x]
            out_final = out1 * out2 * out3
            
            # Hidden layer
            hid1 = out2 * out1 
            hid2 = hid1 * weight0[x]
            hid3 = hidden_layer[x]* (1 - hidden_layer[x])
            hid_final = hid2 * hid3 * in_layer
            
            # weight update
            weight0[x] = weight0[x] - (0.5 * hid_final)
            weight1[x] = weight1[x] - (0.5 * out_final)
    if z % 250 == 0:
        print "MSE: " + str(totalerror / 21.0)
    