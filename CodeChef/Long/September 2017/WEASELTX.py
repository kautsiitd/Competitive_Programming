n,q = map(int,raw_input().split())
graph = [[] for i in range(n)]
for _ in range(n-1):
    a,b = map(int,raw_input().split())
    graph[a].append(b)
    graph[b].append(a)
values = map(int,raw_input().split())

depth = [0 for _ in range(n)]
def dfs(current,parent,currentDepth):
    for child in graph[current]:
        if child != parent:
            depth[child] = currentDepth+1
            dfs(child,current,currentDepth+1)
dfs(0,-1,0)

def numberOfTwosInFactorial(num):
    temp = 2
    ans = 0
    while temp <= num:
        ans += num/temp
        temp*=2
    return ans

queries = [input() for i in range(q)]
for delta in queries:
    ans = values[0]
    for i in range(1,n):
        k1 = numberOfTwosInFactorial(delta-1+depth[i])
        k2 = numberOfTwosInFactorial(depth[i])
        k3 = numberOfTwosInFactorial(delta-1)
        if k1<=k2+k3:
            ans ^= values[i]
    print ans
