import sys
sys.setrecursionlimit(1000000)

n,k = map(int,raw_input().split())
color = [0]+map(int,raw_input().split())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b = map(int,raw_input().split())
    graph[a].append(b)
    graph[b].append(a)

colorQueue = [[] for i in range(max(color)+1)]
sizeOfColorQueue = [0 for i in range(max(color)+1)]
ans = [-1 for i in range(n+1)]

def dfs(current,parent):
    currentColor = color[current]
    if sizeOfColorQueue[currentColor]>=k:
        ans[current] = colorQueue[currentColor][sizeOfColorQueue[currentColor]-k]
    colorQueue[currentColor].append(current)
    sizeOfColorQueue[currentColor] += 1
    for child in graph[current]:
        if child != parent:
            dfs(child,current)
    colorQueue[currentColor].pop()
    sizeOfColorQueue[currentColor] -= 1

dfs(1,0)
for i in ans[1:]:
    print i,
print ""
