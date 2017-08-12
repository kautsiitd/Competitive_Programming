inf = pow(10,25)
def minCost(n,k):
    dp = [[inf for j in range(k+1)] for i in range(n+1)]
    dp[0][0] = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            for m in range(i-1,-1,-1):
                if m == 0:
                    cost = c[i-1]*c[i-1]
                else:
                    cost = (c[i-1]-c[m-1])*(c[i-1]-c[m-1])
                if(inf - cost >= dp[m][j-1]):
                    dp[i][j] = min(dp[i][j], dp[m][j-1]+cost)
    return dp[n][k]


for _ in range(input()):
    n,k,start = map(int,raw_input().split())
    k = min(n,k)
    a = map(int,raw_input().split())
    b = []
    for i in range(1,n):
        b.append(a[i]-a[i-1])
    c = [0];cum = 0
    for i in range(n-1):
        cum += b[i]
        c.append(cum)
    print minCost(n,k)
