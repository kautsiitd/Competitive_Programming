def ansWeight(a):
    return a[-1]-a[-2]

def f(a,b,c,d,x):
    return a*x*x*x + b*x*x + c*x + d

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

for _ in range(input()):
    n = input()
    arr = [[int(i) for i in raw_input()] for _ in range(n)]
    q = 10005
    ans = []
    tempans = []
    # Vertical Lines
    for j in range(n):
        i = 0
        while i<n:
            if arr[i][j] == 1:
                l = i+1
                while i<n and arr[i][j] == 1:
                    i+=1
                r = i
                tempans.append((0,1,0,1,0,1,j+1,l,r))
            else:
                i+=1
    # improveTempAns()

    # Let's try to construct single elements from straight lines
    tempans.sort(key=ansWeight)
    arr = [[0 for j in range(n)] for i in range(n)]
    singlePoints = []
    deleteThese = []
    for ithAns in tempans:
        if ithAns[-1]-ithAns[-2] == 0:
            a,b,c,d,x = ithAns[0],ithAns[2],ithAns[4],ithAns[6],ithAns[7]
            arr[x-1][f(a,b,c,d,x)-1] = 1
            deleteThese.append(ithAns)
    for i in deleteThese:
        tempans.remove(i)

    # Trying single sloped lines, slope = 1
    # tempans = []
    for d in range(-n,n):
        i = 0
        while i < n:
            j = f(0,0,1,d,i)
            if  j<n and j>=0 and arr[i][j] == 1:
                l = i+1
                while i<n and j<n and j>=0 and arr[i][j] == 1:
                    i += 1
                    j = f(0,0,1,d,i)
                r = i
                tempans.append((0,1,0,1,1,1,d,l,r))
            else:
                i += 1
    improveTempAns()

    # Trying single sloped lines, slope = -1
    # not covering whole matrix because d needs to be greater than n
    # tempans = []
    # for offset in range(0,n):
    #     i = 0
    #     while i < n:
    #         j = f(0,0,-1,offset,i)
    #         if  j<n and j>=0 and arr[i][j] == 1:
    #             l = i+1
    #             while i<n and j<n and j>=0 and arr[i][j] == 1:
    #                 i += 1
    #                 j = f(0,0,-1,offset,i)
    #             r = i
    #             tempans.append((0,1,0,1,-1,1,offset,l,r))
    #         else:
    #             i += 1
    # improveTempAns()

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
