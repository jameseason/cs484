# James Eason
# CS 484 Assignment 3
# Windy Gridworld using Sarsa

import random 
import collections

# Create grid with wind values
def getWindGrid():
    windGrid = [[0 for x in range(10)] for y in range(7)]
    for row in range(0, len(windGrid)):
        windGrid[row][3] = 1
        windGrid[row][4] = 1
        windGrid[row][5] = 1
        windGrid[row][6] = 2
        windGrid[row][7] = 2
        windGrid[row][8] = 1
    return windGrid
    
# Get initial values for every state-action tuple
def initMoveValues(grid):
    moveValues = collections.defaultdict(dict)
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            moveValues[(row, col)]["U"] = round(random.uniform(0, 1) *2-1, 3)
            moveValues[(row, col)]["D"] = round(random.uniform(0, 1) *2-1, 3)
            moveValues[(row, col)]["L"] = round(random.uniform(0, 1) *2-1, 3)
            moveValues[(row, col)]["R"] = round(random.uniform(0, 1) *2-1, 3)
    return moveValues

# Get reward value for each state    
def getRewardValues(grid, goal):
    r = {}
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            r[(row, col)] = -1
    r[goal] = 99
    return r
   
# Choose an action based on moveValues
def chooseAction(agentState, mv, e):
    actionVals = mv[agentState]
    moves = ["U", "D", "L", "R"]
    
    # Disallow moves off grid
    if agentState[1] <= 0:
        moves.remove("L")
    if agentState[1] >= 9:
        moves.remove("R")
    if agentState[0] >= 6:
        moves.remove("D")
    if agentState[0] <= 0:
        moves.remove("U")
    
    # Action value of each move
    uval = actionVals["U"]
    dval = actionVals["D"]
    lval = actionVals["L"]
    rval = actionVals["R"]
    
    if (random.uniform(0, 1) <= e) or (uval == dval and dval == lval and lval == rval):
        # Pick a random move if e or everything is equal
        return random.choice(moves)
    else:
        temp = []
        for move in moves:
            temp.append(actionVals[move])
        action = max(temp)
        
        for move in moves:
            if str(actionVals[move]) == str(action):
                return move
    raise RuntimeError("Didn't pick an action?" + str(action) + " " + str(actionVals))

# Move an agent    
def moveAgent(agentState, action, windGrid):
    if action == "D":
        return blowAgent((agentState[0]+1, agentState[1]), windGrid)
    elif action == "U":
        return blowAgent((agentState[0]-1, agentState[1]), windGrid)
    elif action == "L":
        return blowAgent((agentState[0], agentState[1]-1), windGrid)
    elif action == "R":
        return blowAgent((agentState[0], agentState[1]+1), windGrid)

# Apply wind effects to agent after movement
def blowAgent(agentState, windGrid):
    windVal = windGrid[agentState[0]][agentState[1]]
    newRow = agentState[0]-windVal
    if newRow < 0:
        newRow = 0
    return (newRow, agentState[1])
    
# Print updated gridworld
def updateGrid(agentState, goal):
    grid = [["-" for x in range(10)] for y in range(7)]
    grid[goal[0]][goal[1]] = "G"
    grid[agentState[0]][agentState[1]] = "A"
    #for row in grid:
    #    print row
    return grid

lrate = 0.8
discount = 0.7
e = 0.2
windGrid = getWindGrid()

totalmoves=[]
agentState = (3, 0)
goal = (3, 7)
grid = updateGrid(agentState, goal)
moveValues = initMoveValues(grid)
r = getRewardValues(grid, goal)
for x in range(50):
    agentState = (3, 0)
    action = chooseAction(agentState, moveValues, e)
    moves = 0
    grid = updateGrid(agentState, goal)
    while True:
        oldState = agentState
        #print "\nAgent moving in direction: " + action
        agentState = moveAgent(agentState, action, windGrid)
        grid = updateGrid(agentState, goal)
        if (agentState == goal):
            break
        newAction = chooseAction(agentState, moveValues, e)
        #print "next action: " + newAction
        q1 = round(moveValues[oldState][action], 3)
        q2 = round(moveValues[agentState][newAction], 3)
        moveValues[oldState][action] = q1 + lrate * ( r[agentState] + discount * q2 - q1)
        action = newAction
        moves += 1
    totalmoves.append(moves)
    if x == 15:
        e -= 0.1
    if x == 30:
        e -= 0.05
    if x == 45:
        e = 0
print totalmoves
    



