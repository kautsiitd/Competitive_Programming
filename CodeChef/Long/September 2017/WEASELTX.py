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
maxDepth = max(depth)

queries = [input() for i in range(q)]
maxDelta = max(queries)

matrix = [[1] for i in range(maxDelta+1)]
for _ in range(maxDepth):
    matrix[0].append(1)
for i in range(1,maxDelta+1):
    for j in range(1,maxDepth+1):
        matrix[i].append(matrix[i-1][j]^matrix[i][j-1])

for delta in queries:
    ans = values[0]
    for i in range(1,n):
        if matrix[delta-1][depth[i]] == 1:
            ans ^= values[i]
    print ans
