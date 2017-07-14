import itertools
import math

def findRoots(index,tillNowSum):
    global roots,a
    if index == n:
        roots.append(tillNowSum)
    else:
        tillNowSum += a[index]
        findRoots(index+1,tillNowSum)
        tillNowSum -= 2*a[index]
        findRoots(index+1,tillNowSum)

mod = 1000000007
for _ in range(input()):
    n = input()
    a = [math.sqrt(i) for i in map(int,raw_input().split())]
    roots = []
    totalNumberOfRoots = pow(2,n)
    findRoots(0,0)
    cofficients = [0,0]
    currentPoly = [1]
    for index in range(totalNumberOfRoots):
        currentPoly.append(0)
        for i in range(index+1,0,-1):
            currentPoly[i] += currentPoly[i-1]*roots[index]
    print totalNumberOfRoots
    for i in range(totalNumberOfRoots,0,-1):
        print (int(round(currentPoly[i]))%mod + mod)%mod,
    print (int(round(currentPoly[0]))%mod + mod)%mod
