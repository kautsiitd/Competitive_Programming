from itertools import combinations
import sys
sys.setrecursionlimit(1000000)

mod = 1000000007
powTwo = [1]
for _ in range(100005):
    powTwo.append((powTwo[-1]*2)%mod)

def setVariables1():
    global OneEdgeUsingTwoNodes
    global OneEdgeUsingTwoNodesAns
    OneEdgeUsingTwoNodes = e
    OneEdgeUsingTwoNodesAns = powTwo[v-2]*OneEdgeUsingTwoNodes

def setVariables2():
    global TwoEdgeUsingThreeNodes,TwoEdgeUsingFourNodes
    global TwoEdgeUsingThreeNodesAns,TwoEdgeUsingFourNodesAns
    for i in edgeFrom[1:]:
        if(i>=2):
            TwoEdgeUsingThreeNodes += (i*(i-1))/2
    TwoEdgeUsingThreeNodesAns = powTwo[v-3]*TwoEdgeUsingThreeNodes
    if e>=4:
        TwoEdgeUsingFourNodes = (e*(e-1))/2 - TwoEdgeUsingThreeNodes
        TwoEdgeUsingFourNodesAns = powTwo[v-4]*TwoEdgeUsingFourNodes

def setVariables3():
    global ThreeEdgeUsingThreeNodes,ThreeEdgeUsingFourNodes,ThreeEdgeUsingFiveNodes,ThreeEdgeUsingSixNodes
    global ThreeEdgeUsingThreeNodesAns,ThreeEdgeUsingFourNodesAns,ThreeEdgeUsingFiveNodesAns,ThreeEdgeUsingSixNodesAns
    for a in range(1,v+1):
        edgesFromA = edgeFrom[a]
        # For 4 Nodes
        if(edgesFromA >= 3):
            ThreeEdgeUsingFourNodes += (edgesFromA*(edgesFromA-1)*(edgesFromA-2))/6
        # Dependency on connected nodes b and c
        for i in range(edgesFromA):
            b = graph[a][i]
            for j in range(i+1,edgesFromA):
                c = graph[a][j]
                # For 3 Nodes
                if((b,c) in graphDict):
                    ThreeEdgeUsingThreeNodes += 1
                    ThreeEdgeUsingFiveNodes += 1    # Because of connection between b&c
                # For 5 Nodes
                ThreeEdgeUsingFiveNodes += e-edgeFrom[a]-edgeFrom[b]-edgeFrom[c]+2
    ThreeEdgeUsingThreeNodes /= 3
    # For 4 Nodes Straight Lines
    temp = 0
    for a in range(1,v+1):
        edgesFromA = edgeFrom[a]
        for i in range(edgesFromA):
            b = graph[a][i]
            for j in range(edgeFrom[b]):
                c = graph[b][j]
                if c == a:
                    continue
                temp += edgeFrom[c]-1
                if (a,c) in graphDict:
                    temp -= 1
    ThreeEdgeUsingFourNodes += temp/2
    ThreeEdgeUsingSixNodes = (e*(e-1)*(e-2))/6 - (ThreeEdgeUsingThreeNodes+ThreeEdgeUsingFourNodes+ThreeEdgeUsingFiveNodes)
    # print ThreeEdgeUsingThreeNodes,ThreeEdgeUsingFourNodes,ThreeEdgeUsingFiveNodes,ThreeEdgeUsingSixNodes
    if v>=3:
        ThreeEdgeUsingThreeNodesAns = (6*powTwo[v-3]*ThreeEdgeUsingThreeNodes)%mod
    if v>=4:
        ThreeEdgeUsingFourNodesAns = (6*powTwo[v-4]*ThreeEdgeUsingFourNodes)%mod
    if v>=5:
        ThreeEdgeUsingFiveNodesAns = (6*powTwo[v-5]*ThreeEdgeUsingFiveNodes)%mod
    if v>=6:
        ThreeEdgeUsingSixNodesAns = (6*powTwo[v-6]*ThreeEdgeUsingSixNodes)%mod

def customPow(a,b):
    ans = 1
    while b != 0:
        ans *= a
        ans %= mod
        b-=1
    return ans

for _ in range(input()):
    v,e,k = map(int,raw_input().split())
    graph = [[] for __ in range(v+1)]
    edgeFrom = [0 for i in range(v+1)]
    allEdges = []
    graphDict = {}
    for __ in range(e):
        a,b = map(int,raw_input().split())
        graph[a].append(b)
        graph[b].append(a)
        edgeFrom[a] += 1
        edgeFrom[b] += 1
        allEdges.append([a,b])
        graphDict[(a,b)] = True
        graphDict[(b,a)] = True
    for i in range(1,v+1):
        graph[i].sort()
    if v == 1 or e == 0:
        print 0
    elif v == 2:
        print 1
    else:
        # One Edge in expansion
        OneEdgeUsingTwoNodes = 0
        # Two Edges in expansion
            # using 3 nodes
        TwoEdgeUsingThreeNodes = 0
        TwoEdgeUsingThreeNodesAns = 0
            # using 4 nodes
        TwoEdgeUsingFourNodes = 0
        TwoEdgeUsingFourNodesAns = 0
        # Three Edges in expansion
            # using 3 nodes
        ThreeEdgeUsingThreeNodes = 0
        ThreeEdgeUsingThreeNodesAns = 0
            # using 4 nodes
        ThreeEdgeUsingFourNodes = 0
        ThreeEdgeUsingFourNodesAns = 0
            # using 5 nodes
        ThreeEdgeUsingFiveNodes = 0
        ThreeEdgeUsingFiveNodesAns = 0
            # using 6 nodes
        ThreeEdgeUsingSixNodes = 0
        ThreeEdgeUsingSixNodesAns = 0

        if k == 1:
            setVariables1()
            print (OneEdgeUsingTwoNodesAns)%mod
        elif k == 2:
            setVariables1()
            setVariables2()
            TwoEdgeUsingThreeNodesAns = (2*TwoEdgeUsingThreeNodesAns)%mod
            TwoEdgeUsingFourNodesAns = (2*TwoEdgeUsingFourNodesAns)%mod
            print (OneEdgeUsingTwoNodesAns+TwoEdgeUsingThreeNodesAns+TwoEdgeUsingFourNodesAns)%mod
        elif k == 3 and v<=3000:
            setVariables1()
            setVariables2()
            setVariables3()
            TwoEdgeUsingThreeNodesAns = (6*TwoEdgeUsingThreeNodesAns)%mod
            TwoEdgeUsingFourNodesAns = (6*TwoEdgeUsingFourNodesAns)%mod
            # print OneEdgeUsingTwoNodesAns,TwoEdgeUsingThreeNodesAns,TwoEdgeUsingFourNodesAns,ThreeEdgeUsingThreeNodesAns,ThreeEdgeUsingFourNodesAns,ThreeEdgeUsingFiveNodesAns,ThreeEdgeUsingSixNodesAns
            print (OneEdgeUsingTwoNodesAns+TwoEdgeUsingThreeNodesAns+TwoEdgeUsingFourNodesAns+ThreeEdgeUsingThreeNodesAns+ThreeEdgeUsingFourNodesAns+ThreeEdgeUsingFiveNodesAns+ThreeEdgeUsingSixNodesAns)%mod
        else:
            sys.exit()
