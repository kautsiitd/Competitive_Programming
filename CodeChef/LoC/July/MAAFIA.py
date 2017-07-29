n,m,k = map(int,raw_input().split())
graph = {}
for _ in range(m):
    a,b = map(int,raw_input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]
specialNodes = sorted(map(int,raw_input().split()))
isSpecial = [False for i in range(n+1)]
for specialNode in specialNodes:
    isSpecial[specialNode] = True

minDist = n+1
for i in specialNodes:
    visited = {}
    visited[i] = True
    stack = []
    stackSize = 0
    for child in graph[i]:
        stack.append((child,1))
        stackSize += 1
    currentIndex = 0
    while currentIndex < stackSize:
        visited[stack[currentIndex][0]] = True
        if isSpecial[stack[currentIndex][0]]:
            minDist = min(stack[currentIndex][1],minDist)
            break
        elif stack[currentIndex][1] >= minDist:
            break
        else:
            currentLevel = stack[currentIndex][1]
            for child in graph[stack[currentIndex][0]]:
                if not(child in visited):
                    stack.append((child,currentLevel+1))
                    stackSize += 1
            currentIndex += 1

minRadius = (minDist-1)/2
ans = 0
visited = [False for i in range(n+1)]
def dfs(parentNode, currentNode, level):
    global ans
    if level > minRadius:
        return
    else:
        ans += 1
        visited[currentNode] = True
        for child in graph[currentNode]:
            if not(visited[child]):
                dfs(currentNode,child,level+1)

for node in specialNodes:
    dfs(-1,node,0)
print ans
