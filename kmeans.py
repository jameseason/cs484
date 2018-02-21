# James Eason 
# Assignment 2 

import numpy as np
import copy

# Generate random tuples between -10 and 10 inclusive
def getData(size):
    data = []
    for x in range(0, size):
        data.append((np.random.randint(21)-10, np.random.randint(21)-10))
    return data

# Distance between two points
def getDist(point1, point2):
    return np.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
 
# Get the index of the closest centroid to a given point
def getClosestCentroid(centroids, point):
    closestDist=99
    for x in range(0, len(centroids)):
        dist = getDist(centroids[x], point)
        if dist < closestDist:
            closestDist = dist
            closestCentroid = x
    return closestCentroid

# Cluster-ify the data based on the centroids
def getClusters(centroids, data):
    clusters = []
    for centroid in centroids:
        clusters.append([])
    for point in data:
        clusters[getClosestCentroid(centroids, point)].append(point)
    return clusters

# Update centroids based on their clusters    
def updateCentroids(centroids, clusters):
    for x in range(len(clusters)):
        totalX=0.
        totalY=0.
        for element in clusters[x]:
            totalX += element[0]
            totalY += element[1]
        centroids[x] = ((totalX / len(clusters[x])), (totalY / len(clusters[x])))
    return centroids
  
# Initialization    
print "Enter K (4 or 6): "
k = int(raw_input())
np.random.seed(1)
centroids = [(5, 5), (5, -5), (-5, 5), (-5, -5), (0, 5), (0, -5)]
centroids = centroids[0:k]
print "Initialized centroids: " + str(centroids)
# Training data
data = getData(800)

# Will run until centroids stop updating
while True:
    # Get clusters
    clusters = getClusters(centroids, data)
    # Update centroids
    oldCentroids = copy.deepcopy(centroids)
    centroids = updateCentroids(centroids, clusters)
    if oldCentroids == centroids:
        print "Final centroids: " + str(centroids) + "\n\n"
        break
    else:
        print "Updated centroids: " + str(centroids)

# Test data
testData = getData(200)
testClusters = getClusters(centroids, testData)
for x in range(len(testClusters)):
    print "Number of test values in cluster " + str(x) + ": " + str(len(testClusters[x]))
