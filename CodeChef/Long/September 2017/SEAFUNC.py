from itertools import permutations
import random

def ansWeight(a):
    return a[-1]-a[-2]

def f(a,b,c,d,x):
    return a*x*x*x + b*x*x + c*x + d

def findCurves(a,b,c):
    global tempans
    for d in range(-n-1,n+2):
        i = 1
        while i<=n:
            j = f(a,b,c,d,i)
            if j>=1 and j<=n and arr[i-1][j-1] == 1:
                l = i
                pointCount = 0
                while i<=n and j>=1 and j<=n:
                    if arr[i-1][j-1] == 1:
                        i+=1
                        j = f(a,b,c,d,i)
                        pointCount += 1
                    else:
                        if originalArr[i-1][j-1] == 1 and l < i:
                            i+=1
                            j = f(a,b,c,d,i)
                        else:
                            break
                if pointCount > 1:
                    r = i-1
                else:
                    r = l
                tempans.append((a,1,b,1,c,1,d,l,r))
            else:
                i+=1

def reputSinglePoints(newA,newB,newC):
    global arr
    tempans.sort(key=ansWeight)
    arr = [[0 for j in range(n)] for i in range(n)]
    deleteThese = []
    for ithAns in tempans:
        if ithAns[-1]-ithAns[-2] == 0:
            a,b,c,d,x = ithAns[0],ithAns[2],ithAns[4],ithAns[6],ithAns[7]
            y = f(a,b,c,d,x)
            newD = y - (newA*x*x*x + newB*x*x + newC*x)
            if(newD >= -n and newD <= n):
                arr[x-1][y-1] = 1
                deleteThese.append(ithAns)
    for i in deleteThese:
        tempans.remove(i)
    # for i in arr:
    #     print i
    # print ""

# Formatting ans, creating diff at most 100 worst points
def improveTempAns():
    global tempans,ans,q
    tempans.sort(key=ansWeight)
    diff = 0
    i = 0
    for ansElement in tempans:
        if diff + ansWeight(ansElement) + 1 <= 100:
            diff += ansWeight(ansElement)+1
            i += 1
        else:
            break
    tempans = tempans[i:]
    if len(tempans) < q:
        ans = tempans
        q = len(ans)

def resetTempAns():
    global tempans
    tempans = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if originalArr[i-1][j-1] == 1:
                tempans.append([0,1,0,1,0,1,j,i,i])

primeNumbers = [-7,-5,-3,-2,-1,0,1,2,3,5,7]
numberOfPrimeNumbers = len(primeNumbers)

for _ in range(input()):
    n = input()
    originalArr = [[int(i) for i in raw_input()] for _ in range(n)]
    q = 10005
    ans = []

    # Choosing functions randomly
    # numberOfIterations = 2
    # depthOfIteration = 2
    # for iterations in range(numberOfIterations):
    #     arr = originalArr
    #     resetTempAns()
    #     for ithFunc in range(depthOfIteration):
    #         a = primeNumbers[random.randint(0,numberOfPrimeNumbers-1)]
    #         b = primeNumbers[random.randint(0,numberOfPrimeNumbers-1)]
    #         c = primeNumbers[random.randint(0,numberOfPrimeNumbers-1)]
    #         reputSinglePoints(a,b,c)
    #         findCurves(a,b,c)
    #     improveTempAns()

    # Choosing linear function in every order
    orderFrom = -1
    orderTill = 1
    orders = permutations(range(orderFrom,orderTill+1),(orderTill-orderFrom+1))

    for order in orders:
        arr = originalArr
        resetTempAns()
        for i in order:
            reputSinglePoints(0,0,i)
            findCurves(0,0,i)
        reputSinglePoints(0,0,2)
        findCurves(0,0,2)
        reputSinglePoints(0,0,3)
        findCurves(0,0,3)
        reputSinglePoints(0,0,5)
        findCurves(0,0,5)
        reputSinglePoints(0,0,7)
        findCurves(0,0,7)
        improveTempAns()

    # printing ans
    print len(ans)
    for i in ans:
        for j in i:
            print j,
        print ""

    # print "[",
    # for i in ans:
    #     print "(",i[-3],",",i[-2],",",i[-1],"),",
    # print "]"
