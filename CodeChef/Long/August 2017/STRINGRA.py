for _ in range(input()):
    n,m = map(int,raw_input().split())
    edges = sorted([map(int,raw_input().split())[::-1] for __ in range(m)])

    newEdges = [[],[]]
    tempIndex = 0
    for i in range(1,n+1):
        while(tempIndex < m and edges[tempIndex][0] == i):
            newEdges[i].append(edges[tempIndex][1])
            tempIndex += 1
        newEdges.append([])

    canExists = True
    for endNode in newEdges:
        if not(endNode):
            continue
        if not(canExists):
            break
        lastStartNode = endNode[0]
        for i in range(1,len(endNode)):
            startNode = endNode[i]
            if startNode != lastStartNode+1:
                canExists = False
                break
            else:
                lastStartNode = startNode

    if not(canExists):
        print -1
        continue

    criticalPoints = []
    tempI = 1
    for i in newEdges[1:-1]:
        if i and i[-1] == tempI-1:
            criticalPoints.append(i[0])
        else:
            canExists = False
            break
        tempI += 1

    if not(canExists):
        print -1
        continue

    lastIndex = [-1 for i in range(100005)]
    ans = [1]
    lastIndex[ans[0]] = 0

    for i in range(1,n):
        if criticalPoints[i] == 0:
            num = 1
            while lastIndex[num] != -1:
                num += 1
            ans.append(num)
            lastIndex[num] = i
        else:
            num = ans[criticalPoints[i]-1]
            if lastIndex[num] >= criticalPoints[i]:
                canExists = False
                break
            else:
                ans.append(num)
                lastIndex[num] = i

    if canExists:
        for i in ans:
            print i,
        print ""
    else:
        print -1
