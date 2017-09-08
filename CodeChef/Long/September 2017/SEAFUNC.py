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
                while i<=n and j>=1 and j<=n and arr[i-1][j-1] == 1:
                    i+=1
                    j = f(a,b,c,d,i)
                r = i-1
                tempans.append((a,1,b,1,c,1,d,l,r))
            else:
                i+=1

# Formatting ans, creating diff at most 100 worst points
def improveTempAns():
    global tempans,ans,q
    tempans.sort(key=ansWeight)
    diff = 0
    i = 0
    for ansElement in tempans:
        if diff + ansWeight(ansElement) + 1 <= 0:
            diff += ansWeight(ansElement)+1
            i += 1
        else:
            break
    tempans = tempans[i:]
    if len(tempans) < q:
        ans = tempans
        q = len(ans)

for _ in range(input()):
    n = input()
    arr = [[int(i) for i in raw_input()] for _ in range(n)]
    originalArr = [[arr[i][j] for j in range(n)] for i in range(n)]
    q = 10005
    ans = []
    tempans = []
    # Vertical Lines
    findCurves(0,0,0)

    # Reputting single Points
    tempans.sort(key=ansWeight)
    arr = [[0 for j in range(n)] for i in range(n)]
    singlePoints = []
    deleteThese = []
    for ithAns in tempans:
        if ithAns[-1]-ithAns[-2] == 0:
            a,b,c,d,x = ithAns[0],ithAns[2],ithAns[4],ithAns[6],ithAns[7]
            y = f(a,b,c,d,x)
            arr[x-1][y-1] = 1
            deleteThese.append(ithAns)
    for i in deleteThese:
        tempans.remove(i)

    # Trying single sloped lines, slope = 1
    findCurves(0,0,1)

    # Reputting single Points
    tempans.sort(key=ansWeight)
    arr = [[0 for j in range(n)] for i in range(n)]
    singlePoints = []
    deleteThese = []
    for ithAns in tempans:
        if ithAns[-1]-ithAns[-2] == 0:
            a,b,c,d,x = ithAns[0],ithAns[2],ithAns[4],ithAns[6],ithAns[7]
            y = f(a,b,c,d,x)
            if(x+y <= n):
                arr[x-1][y-1] = 1
                deleteThese.append(ithAns)
    for i in deleteThese:
        tempans.remove(i)

    # Trying single sloped lines, slope = -1
    findCurves(0,0,-1)
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
