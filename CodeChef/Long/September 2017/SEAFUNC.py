def ansWeight(a):
    return a[-1]-a[-2]

def f(i,offset):
    return i+offset

# Formatting ans, creating diff at most 100 worst points
def improveTempAns():
    global tempans,ans
    tempans.sort(key=ansWeight)
    diff = 0
    i = 0
    for ansElement in tempans:
        if diff + ansWeight(ansElement) + 1 <= 1:
            diff += ansWeight(ansElement)+1
            i += 1
        else:
            break
    tempans = tempans[i:]
    if len(tempans) < q:
        ans = tempans

for _ in range(input()):
    n = input()
    a = [[int(i) for i in raw_input()] for _ in range(n)]
    q = 10005
    ans = []
    tempans = []
    # Vertical Lines
    for j in range(n):
        i = 0
        while i<n:
            if a[i][j] == 1:
                l = i+1
                while i<n and a[i][j] == 1:
                    i+=1
                r = i
                tempans.append((0,1,0,1,0,1,j+1,l,r))
            else:
                i+=1
    improveTempAns()

    # Trying single sloped lines
    tempans = []
    for offset in range(-n,n):
        i = 0
        while i < n:
            if f(i,offset) < n and f(i,offset) >= 0 and a[i][f(i,offset)] == 1:
                l = i+1
                while i<n and f(i,offset) < n and f(i,offset) >= 0 and a[i][f(i,offset)] == 1:
                    i += 1
                r = i
                tempans.append((0,1,0,1,1,1,offset,l,r))
            else:
                i += 1
    improveTempAns()

    # printing ans
    print len(ans)
    for i in ans:
        for j in i:
            print j,
        print ""
