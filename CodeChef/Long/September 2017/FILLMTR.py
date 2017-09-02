import sys
sys.setrecursionlimit(100000000)

def dfs(current,parent):
    global answer,answerFound
    for child in children[current]:
        if child != parent:
            if visited[child]:
                if value[child] != abs(value[current]-edges[(current,child)]):
                    answer = "no"
                    answerFound = True
            else:
                value[child] = abs(value[current]-edges[(current,child)])
                visited[child] = True
                dfs(child,current)

for _ in range(input()):
    n,q = map(int,raw_input().split())
    edges = {}
    children = [[] for i in range(n+1)]
    answer = "yes"
    answerFound = False
    for _ in range(q):
        a,b,v = map(int,raw_input().split())
        if a==b:
            if v == 0:
                continue
            else:
                answer = "no"
                answerFound = True
        if (a,b) in edges and edges[(a,b)] != v:
            answer = "no"
            answerFound = True
        else:
            edges[(a,b)] = v
            edges[(b,a)] = v
            children[a].append(b)
            children[b].append(a)
    if answerFound:
        print "no"
        continue
    visited = [False for _ in range(n+1)]
    value = [-1 for _ in range(n+1)]
    for i in range(1,n+1):
        if not(visited[i]) and not(answerFound):
            visited[i] = True
            value[i] = 0
            dfs(i,-1)
    print answer
