def ansWeight(a):
    return a[-1]-a[-2]

def f(i,offset):
    return i+offset

for _ in range(input()):
    n = input()
    a = [[int(i) for i in raw_input()] for _ in range(n)]
    ans = []
    # Combining range
    for j in range(n):
        i = 0
        while i<n:
            if a[i][j] == 1:
                l = i+1
                while i<n and a[i][j] == 1:
                    i+=1
                r = i
                ans.append((0,1,0,1,0,1,j+1,l,r))
            else:
                i+=1

    # Formatting ans, creating diff at most 100 worst points
    ans.sort(key=ansWeight)
    diff = 0
    i = 0
    for ansElement in ans:
        if diff + ansWeight(ansElement) + 1 <= 100:
            diff += ansWeight(ansElement)+1
            i += 1
        else:
            break
    ans = ans[i:]

    # Trying single sloped lines
    ans1 = []
    for offset in range(-n,n):
        i = 0
        while i < n:
            if f(i,offset) < n and f(i,offset) >= 0 and a[i][f(i,offset)] == 1:
                l = i+1
                while i<n and f(i,offset) < n and f(i,offset) >= 0 and a[i][f(i,offset)] == 1:
                    i += 1
                r = i
                ans1.append((0,1,0,1,1,1,offset,l,r))
            else:
                i += 1

    # Formatting ans1, creating diff at most 100 worst points
    ans1.sort(key=ansWeight)
    diff = 0
    i = 0
    for ansElement in ans1:
        if diff + ansWeight(ansElement) + 1 <= 100:
            diff += ansWeight(ansElement)+1
            i += 1
        else:
            break
    ans1 = ans1[i:]

    # printing ans
    if len(ans1) < len(ans):
        print len(ans1)
        for i in ans1:
            for j in i:
                print j,
            print ""
    else:
        print len(ans)
        for i in ans:
            for j in i:
                print j,
            print ""
