import collections
import sys
sys.setrecursionlimit(1000000)

mod = 1000000007
powTwo = [1]
for _ in range(100005):
    powTwo.append((powTwo[-1]*2)%mod)

def customPow(a,b):
    ans = 1
    while b != 0:
        ans *= a
        ans %= mod
        b-=1
    return ans

def dfs(currentVertex,currentEdges):
    global ans
    if currentVertex > v:
        return
    visited[currentVertex] = True
    i=1
    while currentVertex+i <= v and visited[currentVertex+i]:
        i+=1
    dfs(currentVertex+i,currentEdges)
    included[currentVertex] = True
    newEdges = sum([1 for child in graph[currentVertex] if included[child]])
    currentEdges += newEdges
    currentEdges %= mod
    value = customPow(currentEdges,k)%mod
    ans += value
    ans %= mod
    while currentVertex+i <= v and visited[currentVertex+i]:
        i+=1
    dfs(currentVertex+i,currentEdges)
    visited[currentVertex] = False
    included[currentVertex] = False

for _ in range(input()):
    v,e,k = map(int,raw_input().split())
    graph = [[] for __ in range(v+1)]
    for __ in range(e):
        a,b = map(int,raw_input().split())
        graph[a].append(b)
        graph[b].append(a)
    if v == 1:
        print 0
    else:
        if k == 1:
            print (powTwo[v-2]*e)%mod
        else:
            ans = 0
            visited = [False for i in range(v+1)]
            included = [False for i in range(v+1)]
            dfs(1,0)
            print ans
