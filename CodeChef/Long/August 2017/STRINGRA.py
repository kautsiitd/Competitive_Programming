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

    numNotLie = []
    for i in range(1,n+1):
        numNotLie.append([newEdges[i][0]+1,i-1])

    ans = [0]
    print newEdges
    print numNotLie
    for notLieRange in numNotLie:
        if notLieRange[0]>notLieRange[1]:
            ans.append(1)
            continue
        num = 1
        temp = ans[notLieRange[0]:notLieRange[1]+1]
        print temp
        while num in temp:
            num += 1
        ans.append(num)

    for i in ans[1:]:
        print i,
    print ""
