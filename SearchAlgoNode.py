class Node:
    #Initializing node attributes
    def __init__(self, curState, curParent, distCost, nodeHeuristics, curAlgorithm):
        self.CURSTATE = curState
        self.CURPARENT = curParent
        self.DISTCOST = distCost
        self.NODEHEURISTICS = nodeHeuristics
        if curAlgorithm == 'GBestFSearch':
            self.INFO = self.NODEHEURISTICS
        elif curAlgorithm == 'A*':
            self.INFO = self.DISTCOST + self.NODEHEURISTICS

    #returns the cost of path
    def getDistCost(self):
        return self.DISTCOST
    
    #returns algorithm info
    def getInfo(self):
        return self.INFO

    #returns state
    def getCurState(self):
        return self.CURSTATE

    #returns parent
    def getCurParent(self):
        return self.CURPARENT

    #returns heuristics
    def getNodeHeuristics(self):
        return self.NODEHEURISTICS

    def __lt__(self, other):
        return self.getInfo() < other.getInfo()

    def __le__(self, other):
        return self.getInfo() <= other.getInfo()

    def __gt__(self, other):
        return self.getInfo() > other.getInfo()

    def __ge__(self, other):
        return self.getInfo() >= other.getInfo()

    def __eq__(self, other):
        return self.getInfo() == other.getInfo()

    def __hash__(self):
        return hash(self.getCurState)
