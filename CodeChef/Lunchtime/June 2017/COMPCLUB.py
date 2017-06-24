p = []
def isAncestor(a,b):
    if b == 0 or p[b-1] == b:
        return False
    elif p[b-1] == a:
        return True
    else:
        return isAncestor(a,p[b-1])

for _ in range(input()):
    n,x = map(int,raw_input().split())
    p = map(int,raw_input().split())
    c = map(int,raw_input().split())
    k = map(int,raw_input().split())

    levelMap = {}
    for i in range(n):
        if k[i] in levelMap:
            levelMap[k[i]].append(i)
        else:
            levelMap[k[i]] = [i]

    clubMap = {}
    for i in range(n):
        if c[i] in clubMap:
            clubMap[c[i]].append(i)
        else:
            clubMap[c[i]] = [i]

    answerMap = {}
    for i in range(x):
        if not(i in levelMap):
            continue
        for sameLevelMember in levelMap[i]:
            if i == 0:
                answerMap[sameLevelMember] = 1
            else:
                localAnswer = 0
                currentClub = c[sameLevelMember]
                if i-1 in levelMap:
                    for children in levelMap[i-1]:
                        if children in clubMap[currentClub] and isAncestor(sameLevelMember,children):
                            localAnswer+=answerMap[children]
                            localAnswer%=1000000007
                    answerMap[sameLevelMember] = localAnswer
                else:
                    answerMap[sameLevelMember] = 0

    for i in range(n):
        print answerMap[i]
