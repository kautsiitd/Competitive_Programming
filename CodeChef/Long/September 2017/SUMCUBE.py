from itertools import combinations
import sys
sys.setrecursionlimit(1000000)

mod = 1000000007
powTwo = [1]
for _ in range(100005):
    powTwo.append((powTwo[-1]*2)%mod)

def setVariables3():
    global ThreeEdgeUsingThreeNodes,ThreeEdgeUsingFourNodes,ThreeEdgeUsingFiveNodes,ThreeEdgeUsingSixNodes
    global ThreeEdgeUsingThreeNodesAns,ThreeEdgeUsingFourNodesAns,ThreeEdgeUsingFiveNodesAns,ThreeEdgeUsingSixNodesAns
    for triplet in combinations(allEdges,3):
        elements = []
        for i in triplet:
            for j in i:
                elements.append(j)
        elements = list(set(elements))
        l = len(elements)
        # print triplet,l
        if l == 3:
            ThreeEdgeUsingThreeNodes += 1
        elif l == 4:
            ThreeEdgeUsingFourNodes += 1
        elif l == 5:
            ThreeEdgeUsingFiveNodes += 1
        else:
            ThreeEdgeUsingSixNodes += 1
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
    for __ in range(e):
        a,b = map(int,raw_input().split())
        graph[a].append(b)
        graph[b].append(a)
        edgeFrom[a] += 1
        edgeFrom[b] += 1
        allEdges.append([a,b])
    if v == 1 or e == 0:
        print 0
    elif v == 2:
        print 1
    else:
        # One Edge in expansion
        singleEdgeAns = (powTwo[v-2]*e)%mod
        # Two Edges in expansion
            # using 3 nodes
        commonNodeEdgePairs = sum([(i*(i-1))/2 for i in edgeFrom[1:]])
        commonNodeTwoEdgesAns = powTwo[v-3]*commonNodeEdgePairs
            # using 4 nodes
        noCommonNodeTwoEdgesAns = 0
        if e>=4:
            noCommonNodeEdgePairs = (e*(e-1))/2 - commonNodeEdgePairs
            noCommonNodeTwoEdgesAns = powTwo[v-4]*noCommonNodeEdgePairs
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
            print singleEdgeAns
        elif k == 2:
            commonNodeTwoEdgesAns = (2*commonNodeTwoEdgesAns)%mod
            noCommonNodeTwoEdgesAns = (2*noCommonNodeTwoEdgesAns)%mod
            print (singleEdgeAns+commonNodeTwoEdgesAns+noCommonNodeTwoEdgesAns)%mod
        elif k == 3 and v<=300:
            setVariables3()
            commonNodeTwoEdgesAns = (6*commonNodeTwoEdgesAns)%mod
            noCommonNodeTwoEdgesAns = (6*noCommonNodeTwoEdgesAns)%mod
            # print singleEdgeAns,commonNodeTwoEdgesAns,noCommonNodeTwoEdgesAns,ThreeEdgeUsingThreeNodesAns,ThreeEdgeUsingFourNodesAns,ThreeEdgeUsingFiveNodesAns,ThreeEdgeUsingSixNodesAns
            print (singleEdgeAns+commonNodeTwoEdgesAns+noCommonNodeTwoEdgesAns+ThreeEdgeUsingThreeNodesAns+ThreeEdgeUsingFourNodesAns+ThreeEdgeUsingFiveNodesAns+ThreeEdgeUsingSixNodesAns)%mod
        else:
            sys.exit()
