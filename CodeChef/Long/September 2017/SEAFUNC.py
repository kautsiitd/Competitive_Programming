def f(a):
    return a[-1]-a[-2]

for _ in range(input()):
    n = input()
    a = [[int(i) for i in raw_input()] for _ in range(n)]
    ans = []
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
    ans.sort(key=f)
    diff = 0
    i = 0
    for ansElement in ans:
        if diff + f(ansElement) + 1 <= 100:
            diff += f(ansElement)+1
            i += 1
        else:
            break
    ans = ans[i:]
    
    # printing ans
    print len(ans)
    for i in ans:
        for j in i:
            print j,
        print ""
