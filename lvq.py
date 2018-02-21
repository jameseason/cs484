# James Eason
# Assignment 2

import numpy as np

# Distance between two points
def getDist(point1, point2):
    return np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Initialization
np.random.seed(1)
pVals = [[-5,5], [0,5], [5,5], [-5,-5], [0,-5], [5,-5]]
outLayer = ['A', 'B', 'C', 'C', 'B', 'A']
inputs = []
inputCategories = []
for pVal in pVals:
    for input in range(100):
        newInput = []
        for v in pVal:
            newInput.append(np.random.uniform(v - 2.5, v + 2.5))
        inputs.append(newInput)
        inputCategories.append(outLayer[pVals.index(pVal)])
# Weights
print "Initial weights: "
weights1 = []
for pVal in pVals:
    weights1.append([np.random.random()*2-1, np.random.random()*2-1])
    print str(pVal) + ": " + str(weights1[-1])
    
# Training
minWeightChange = 0.05 # Stop after weight changes get this small
learnRate = 0.1
done = False
while not done:
    print "runnin"
    for x in range(len(inputs)):
        # Get closest weight index
        closestDist = 99
        for weight in weights1:
            dist = getDist(inputs[x], weight)
            if dist < closestDist:
                closestDist = dist
                closestIndex = weights1.index(weight)
                
        # Calculate new weight
        if outLayer[closestIndex] == inputCategories[x]:
            movement = 1
        else:
            movement = -1
        newWeight = []
        for valIndex in range(len(inputs[x])):
            newWeight.append(weights1[closestIndex][valIndex] + movement * 
                learnRate * (inputs[x][valIndex] - weights1[closestIndex][valIndex]))
                
        # Check if weight changed enough        
        weightChange = getDist(weights1[closestIndex], newWeight)
        if weightChange <= minWeightChange:
            done = True
            
        # Update weight
        weights1[closestIndex] = newWeight
        
print "\nFinal weights:"
for weight in range(len(weights1)):
    print str(pVals[weight]) + ": " + str(weights1[weight])
    
    
# Testing
numTestVals = 450.
testInputs = []
testInputCategories = []
# Generate test data
for pVal in pVals:
    for input in range(numTestVals/6):
        newInput = []
        for v in pVal:
            newInput.append(np.random.uniform(v - 2.5, v + 2.5))
        testInputs.append(newInput)
        testInputCategories.append(outLayer[pVals.index(pVal)])
# Check accuracy
correct = 0
for x in range(len(testInputs)):
    # Get closest weight index
    closestDist = 99
    for weight in weights1:
        dist = getDist(testInputs[x], weight)
        if dist < closestDist:
            closestDist = dist
            closestIndex = weights1.index(weight)
    if outLayer[closestIndex] == testInputCategories[x]:
        correct += 1
print "Correct: " + str(correct/numTestVals)

    