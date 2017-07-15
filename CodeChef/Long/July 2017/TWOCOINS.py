import sys
sys.setrecursionlimit(100010)

def findAnswer(nodeNumber):
    global totalCoinsRequired, visited
    visited[nodeNumber] = True
    # leaf Node
    if numberOfNeighbourhoods[nodeNumber] == 1 and nodeNumber != 1:
        # print "marked: ",nodeNumber
        totalCoinsRequired += 1
        # need 1 at firstLevelChild and can help by 1 fromDistance 1
        return [FlexibleRequirements(1,0), HardRequirements(0,0), CanHelp(1,0)]
    flexibleRequirements = FlexibleRequirements(0,0)
    hardRequirements = HardRequirements(0,0)
    canHelp = CanHelp(0,0)
    for child in tree[nodeNumber]:
        # print "tracing nodeNumber: ",nodeNumber," Child: ",child
        if visited[child]:
            continue
        result = findAnswer(child)
        flexibleRequirements.oneLevel += result[0].oneLevel
        flexibleRequirements.twoLevel += result[0].twoLevel
        hardRequirements.oneLevel += result[1].oneLevel
        hardRequirements.twoLevel += result[1].twoLevel
        canHelp.oneLevel += result[2].oneLevel
        canHelp.twoLevel += result[2].twoLevel

    # root Node
    if nodeNumber == 1:
        # any help is required at level one or two then place coin here
        if flexibleRequirements.oneLevel != 0 or flexibleRequirements.twoLevel != 0 or hardRequirements.oneLevel != 0 or hardRequirements.twoLevel != 0:
            # print "marked: ",nodeNumber
            totalCoinsRequired += 1
        # It is necessary for root that It's requirement should be completed by two level children
        # Otherwise atleast one coin is required for sure because It cannot delay requirement to parent
        elif canHelp.oneLevel < 2:
            # print nodeNumber
            totalCoinsRequired += 1
        return
    # Middle Nodes (other than root and leaf nodes)
    else:
        # It has to have a coin if twoLevel node require some Coin or oneLevel hard requirement is there
        if flexibleRequirements.twoLevel > 0 or hardRequirements.oneLevel > 0 or hardRequirements.twoLevel > 0:
            # print "marked: ",nodeNumber
            totalCoinsRequired += 1
            # After placing coin here, Two level requirements will be finished
            # One Level requirements will be finished too because we moving towards parent from here
            # But if it does not have help at levelOne and levelTwo then It will require help from parent
            if canHelp.oneLevel == 0 and canHelp.twoLevel == 0:
                return [FlexibleRequirements(1,0), HardRequirements(0,0), CanHelp(1,0)]
            # But if there is any help at level one or two then there is no requirements because one coin is already placed
            # and can help by 1 from levelOne and levelOne helps will be levelTwo Helps now
            else:
                return [FlexibleRequirements(0,0), HardRequirements(0,0), CanHelp(1,canHelp.oneLevel)]
        # If one level flexible requirement is there then placing coin will be dependent and can be passed to parent
        elif flexibleRequirements.oneLevel > 0:
            # placing coin will depend on it's own requirements
            # if there is no help at level one at all then it has to have a coin
            if canHelp.oneLevel == 0:
                # this will remove all requirement at below levels
                totalCoinsRequired += 1
                # But if levelTwo help is also not there then It has to ask for help from parent
                if canHelp.twoLevel == 0:
                    return [FlexibleRequirements(1,0), HardRequirements(0,0), CanHelp(1,canHelp.oneLevel)]
                # If there is help at level two then there is no need to ask for help from parent
                else:
                    return [FlexibleRequirements(0,0), HardRequirements(0,0), CanHelp(1,canHelp.oneLevel)]
            # If there is only one help at level 1 then level two help will not require
            # and it's own second necessity can be passed to parent in terms of hardRequirement
            # and if we are passing hardRequirement at level one then there is no need to ask of flexibleRequirements
            elif canHelp.oneLevel == 1:
                return [FlexibleRequirements(0,0), HardRequirements(1,0), CanHelp(0,canHelp.oneLevel)]
            # If one level help is sufficient for this node then there is no requirement to place coin here
            # and below flexibleRequirement can be passed to parent in terms of hardRequirement at level 2
            else:
                return [FlexibleRequirements(0,0), HardRequirements(0,flexibleRequirements.oneLevel), CanHelp(0,canHelp.oneLevel)]
        # There is no requirement at level one or level two
        else:
            # if there is no help at level one at all then it has to have a coin
            if canHelp.oneLevel == 0:
                # print "marked: ",nodeNumber
                totalCoinsRequired += 1
                # But if levelTwo help is also not there then It has to ask for help from parent
                if canHelp.twoLevel == 0:
                    return [FlexibleRequirements(1,0), HardRequirements(0,0), CanHelp(1,canHelp.oneLevel)]
                # If there is help at level two then there is no need to ask for help from parent
                else:
                    return [FlexibleRequirements(0,0), HardRequirements(0,0), CanHelp(1,canHelp.oneLevel)]
            # If there is only one help at level 1 then level two help will not require
            # and it's own second necessity can be passed to parent in terms of hardRequirement
            elif canHelp.oneLevel == 1:
                return [FlexibleRequirements(0,0), HardRequirements(1,0), CanHelp(0,canHelp.oneLevel)]
            # If one level help is sufficient for this node then there is no requirement to place coin here
            # and there is no help is required from parent
            else:
                return [FlexibleRequirements(0,0), HardRequirements(0,0), CanHelp(0,canHelp.oneLevel)]

class HardRequirements(object):
    def __init__(self, oneLevel, twoLevel):
        self.oneLevel = oneLevel
        self.twoLevel = twoLevel

class FlexibleRequirements(object):
    def __init__(self, oneLevel, twoLevel):
        self.oneLevel = oneLevel
        self.twoLevel = twoLevel

class CanHelp(object):
    def __init__(self, oneLevel, twoLevel):
        self.oneLevel = oneLevel
        self.twoLevel = twoLevel

for _ in range(input()):
    n = input()
    if n == 1:
        print -1
        continue
    tree = {}
    for __ in range(n-1):
        a,b = map(int,raw_input().split())
        if a not in tree:
            tree[a] = [b]
        else:
            tree[a].append(b)
        if b not in tree:
            tree[b] = [a]
        else:
            tree[b].append(a)

    numberOfNeighbourhoods = {}
    for node in tree:
        numberOfNeighbourhoods[node] = len(tree[node])

    totalCoinsRequired = 0
    visited = [False for i in range(n+1)]
    # print tree
    # print numberOfNeighbourhoods
    findAnswer(1)
    print totalCoinsRequired
