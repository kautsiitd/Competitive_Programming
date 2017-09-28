def findAns(a,b):
    m = len(a)
    n = len(b)
    l = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j] = 0
            elif a[i-1] == b[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])
    return l[m][n]

for _ in range(input()):
    a = map(int,raw_input().split())[:-1]
    ans = 0
    b = map(int,raw_input().split())[:-1]
    while b!=[]:
        ans = max(ans,findAns(a,b))
        b = map(int,raw_input().split())[:-1]
    print ans
