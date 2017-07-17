import sys
import heapq

# Data Structures
class ServerData(object):
    def __init__(self, serverNumber, cordX, cordY, numberOfComputers, compsPower):
        self.serverNumber = serverNumber
        self.x = cordX
        self.y = cordY
        self.numberOfComputers = numberOfComputers
        self.compsPower = compsPower

class ComputerData(object):
    def __init__(self, serverNumber, computerNumber, cordX, cordY, capacity):
        self.serverNumber = serverNumber
        self.computerNumber = computerNumber
        self.x = cordX
        self.y = cordY
        self.capacity = capacity
        self.timeToHire = 0

# Initialising Input and Storing required Info in defined Structures
totalServers,q = map(int, raw_input().split())

slowestCapacity = 0 #max time taken by computer
maxCaveSizeX = 0
maxCaveSizeY = 0
serversData = []
for serverIndex in range(totalServers):
    inputData = map(int, raw_input().split())
    serverData = ServerData(serverIndex+1,
                            inputData[0],
                            inputData[1],
                            inputData[2],
                            inputData[3:])
    slowestCapacity = max(slowestCapacity, max(serverData.compsPower))
    maxCaveSizeX = max(maxCaveSizeX, serverData.x)
    maxCaveSizeY = max(maxCaveSizeY, serverData.y)
    serversData.append(serverData)

# Deciding various weights
distWeight = 1
capacityWeight = -1
timeWeight = -1
# single server
if totalServers == 1:
    distWeight = 0          #weight of coordinates of computer
    capacityWeight = -1      #weight of speed of computer
    timeWeight = -1         #weight in case of computer is busy
# small Network
elif totalServers <= 100:
    distWeight = 1
    capacityWeight = -2
    timeWeight = -1
# small numberOfTasks
elif q <= 1000:
    distWeight = 2
    capacityWeight = -2
    timeWeight = -0.5
# fast Network
elif slowestCapacity <= 1000:
    distWeight = 2
    capacityWeight = -0.5
    timeWeight = -1
# small Batcave
elif maxCaveSize <= 3000:
    distWeight = 0.5
    capacityWeight = -2
    timeWeight = -1

# making weighted heap for computers
def findWeightOfComp(compData, currentTime):
    global distWeight, capacityWeight, timeWeight
    coordinateWeightage = (compData.x*(maxCaveSizeX - compData.x) + compData.y*(maxCaveSizeY - compData.y))*distWeight
    capacityWeightage = compData.capacity*capacityWeight
    timeWeightage = (compData.timeToHire - currentTime)*timeWeight
    totalWeight = coordinateWeightage + capacityWeightage + timeWeightage
    return totalWeight

weightedHeap = []
for serverData in serversData:
    for compIndex in range(serverData.numberOfComputers):
        compPower = serverData.compsPower[compIndex]
        compData = ComputerData(serverData.serverNumber,
                                compIndex + 1,
                                serverData.x,
                                serverData.y,
                                compPower)
        heapq.heappush(weightedHeap, (-findWeightOfComp(compData, 0), compData))

# asking for queries
for currentTime in range(q):
    print "?"
    sys.stdout.flush()
    taskX, taskY = map(int,raw_input().split())

    unUsableComps = []
    bestComp = heapq.heappop(weightedHeap)[1]
    while bestComp.timeToHire > currentTime:
        unUsableComps.append(bestComp)
        bestComp = heapq.heappop(weightedHeap)[1]
    bestComp.timeToHire = currentTime + bestComp.capacity
    unUsableComps.append(bestComp)

    for comp in unUsableComps:
        heapq.heappush(weightedHeap, (-findWeightOfComp(comp, currentTime), comp))

    print "! " + str(bestComp.serverNumber) + " " + str(bestComp.computerNumber)
    sys.stdout.flush()

print "end"
