import sys
sys.setrecursionlimit(1000000)

upperLimit = pow(10,20)
def findAns(currentIndex,timeRemaining,tempS):
    if timeRemaining == 0:
        return upperLimit
    elif currentIndex == 0:
        return tempS*tempS
    else:
        tempS += a[currentIndex]-a[currentIndex-1]
        temp1 = (tempS*tempS)+findAns(currentIndex-1,timeRemaining-1,0)
        temp2 = findAns(currentIndex-1,timeRemaining,tempS)
        return min(temp1,temp2)

for _ in range(input()):
    n,b,c = map(int,raw_input().split())
    a = map(int,raw_input().split())
    print findAns(n-1,b,0)
