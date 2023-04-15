import csv
import SearchAlgoNode
import sys
from queue import PriorityQueue
from timeit import default_timer

#Creating Empty Variables for straightline csv and driving csv data to be put in
drivingCost = {}
straightLine = {}

#Inputting straightline data in straightLine{}
straightlinecsv = csv.DictReader(open('straightline.csv'))
for row in straightlinecsv:
    straightline = []
    for x in row:
        if x != 'STATE':
            distance = int(row[x])
            if distance > 0:
                straightline.append((x, distance))
    straightLine[row['STATE']] = straightline

#Inputting driving data in drivingCost{}
drivingcsv = csv.DictReader(open('driving.csv'))
for row in drivingcsv:
    driving = []
    for x in row:
        if x != 'STATE':
            distance = int(row[x])
            if distance > 0:
                driving.append((x, distance))
    drivingCost[row['STATE']] = driving

#Get heuristics of initial and goal
def getHeuristics(state_initial: str, state_goal: str):
    currentHeuristic = straightLine[state_initial]
    for state, distance in currentHeuristic:
        if state == state_goal:
            return distance
    return -1

#Expands tree
def expandTree(node, goal):
    nodelist = []
    nodeneighbor = drivingCost[node.getCurState()]
    for z in nodeneighbor:
        first = z[0]
        cost = z[1] + node.getDistCost()
        last = SearchAlgoNode.Node(first, node, cost, getHeuristics(first, goal), 'GBestFSearch')
        nodelist.append(last)
    return nodelist

#A* algorithm that takes initial and goal states and returns a valid path
def aStarAlgorithm(initial, goal):
    
    #initial and final are set
    initialStart = SearchAlgoNode.Node(initial, None, 0, 0, 'A*')
    finalDestination = SearchAlgoNode.Node(goal, None, 0, 0, 'A*')

    #Checks to see if there are valid input states
    if (initial and goal) not in (drivingCost and straightLine):
        return ('FAILED: NO PATH WAS FOUND', 0)
    
    #Initializing a priority queue
    seen = set()
    priorityQueue = PriorityQueue()
    priorityQueue.put((initialStart.getInfo(), initialStart))

    #Loop runs through tree and follows lowest cost while also considering heuristics 
    while not priorityQueue.empty():
        current = priorityQueue.get()[1]
        seen.add(current.getCurState())
        if current.getCurState() == finalDestination.getCurState():
            path = []
            distCost = current.getDistCost()
            while current != initialStart:
                path.append(current.getCurState())
                current = current.getCurParent()
            path.append(initialStart.getCurState())
            return (path[::-1], distCost)
        for c in expandTree(current, goal):
            p = c.getCurState()
            destined = dict.fromkeys(seen, 1)
            if c not in seen or c.getInfo() < destined[p].getInfo():
                destined[p] = c
                priorityQueue.put((c.getDistCost() + c.getNodeHeuristics(), c))

#GBFS algorithm that takes initial and goal states and returns a valid path
def GBestFSearch(initial: str, goal: str):
    
    #initial and final are set
    initialStart = SearchAlgoNode.Node(initial, None, 0, 0, 'GBestFSearch')
    finalDestination = SearchAlgoNode.Node(goal, None, 0, 0, 'GBestFSearch')

    #Checks to see if there are valid input states
    if (initial and goal) not in (drivingCost and straightLine):
        return ('FAILED: NO PATH WAS FOUND', 0)

    #Initializing a priority queue
    seen = set()
    priorityQueue = PriorityQueue()
    priorityQueue.put((initialStart.getInfo(), initialStart))

    #loop runs through tree and follows lowest cost and associates nodes
    while not priorityQueue.empty():
        current = priorityQueue.get()[1]
        seen.add(current.getCurState())
        if current.getCurState() == finalDestination.getCurState():
            path = []
            distCost = current.getDistCost()
            while current != initialStart:
                path.append(current.getCurState())
                current = current.getCurParent()
            path.append(initialStart.getCurState())
            return (path[::-1], distCost)
        for c in expandTree(current, goal):
            p = c.getCurState()
            reached = dict.fromkeys(seen, 1)
            if c not in seen or c.getInfo() < reached[p].getInfo():
                reached[p] = c
                priorityQueue.put((c.getInfo(), c))

#When running searchalgo.py if the amount of arguments inputted is not 3 then error occurs
numArg = len(sys.argv)
if (numArg != 3):
    raise Exception('ERROR: Not enough or too many input arguments.')
print("\nNumber of arguments passed", numArg)

#Argument 1 is set to my name and A number
argumentOne = sys.argv[0]
print('Omar, Hakawati solution:')

#Argument 2 is set to the initial state inputted
argumentTwo = sys.argv[1]
print("Initial State:", argumentTwo)

#Argument 3 is set to the goal state inputted
argumentThree = sys.argv[2]
print('Goal State:', argumentThree)

#Timer is started when GBFS is called, results are displayed
startTime = default_timer()
print('\nGreedy Best First Search:')
print('Solution Path:' + str(GBestFSearch(argumentTwo, argumentThree)[0]))
endTime = default_timer()
overallTime = endTime - startTime
if (GBestFSearch(argumentTwo, argumentThree)[0] == 'FAILED: NO PATH WAS FOUND'):
    print('Number Of States On A Path: ' + str(0))
else:
    print('Number Of States On A Path: ' + str(len(GBestFSearch(argumentTwo, argumentThree)[0])))
print('Path Cost: ' + str(GBestFSearch(argumentTwo, argumentThree)[1]))
print('Execution Time: ' + str(overallTime) + ' Seconds')

#Timer is started when A* is called, results are displayed
startTime2 = default_timer()
print('\nA* Search:')
print('Solution path: ' + str(aStarAlgorithm(argumentTwo, argumentThree)[0]))
timeEnd2 = default_timer()
overallTime2 = timeEnd2 - startTime2
if (aStarAlgorithm(argumentTwo, argumentThree)[0] == 'FAILURE: NO PATH FOUND'):
    print('Number Of States On A Path: ' + str(0))
else:
    print('Number Of States On A Path: ' + str(len(aStarAlgorithm(argumentTwo, argumentThree)[0])))
print('Path Cost: ' + str(aStarAlgorithm(argumentTwo, argumentThree)[1]))
print('Execution Time: ' + str(overallTime2) + ' Seconds')