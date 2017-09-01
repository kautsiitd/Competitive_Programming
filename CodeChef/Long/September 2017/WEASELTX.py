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

evenDepthXor = 0
oddDepthXor = 0
for i in range(1,n):
    if depth[i]%2 == 0:
        evenDepthXor ^= values[i]
    else:
        oddDepthXor ^= values[i]
for _ in range(q):
    delta = input()
    if(delta%4 == 0):
        print values[0]
    elif(delta%4 == 1):
        print values[0]^evenDepthXor^oddDepthXor
    elif(delta%4 == 2):
        print values[0]^evenDepthXor
    elif(delta%4 == 3):
        print values[0]^oddDepthXor
