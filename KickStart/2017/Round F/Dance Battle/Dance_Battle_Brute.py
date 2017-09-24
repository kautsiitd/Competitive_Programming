def printIt(i,ans):
    print "Case #" + str(i+1) + ":",ans

def findSol(currentIndex, currentPower, currentHonor):
    global ans
    if currentIndex == n:
        if currentPower > 0:
            ans = max(ans,currentHonor)
        return
    else:
        findSol(currentIndex+1, currentPower, currentHonor)
        findSol(currentIndex+1, currentPower+powerOf[currentIndex], currentHonor-1)
        findSol(currentIndex+1, currentPower-powerOf[currentIndex], currentHonor+1)

for _ in range(input()):
    e,n = map(int,raw_input().split())
    powerOf = sorted(map(int,raw_input().split()))
    ans = 0
    findSol(0,e,0)
    printIt(_,ans)
