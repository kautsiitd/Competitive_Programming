n,m=map(int,raw_input().split())
colour=[]
for i in range(m+1):
    colour.append([])
    for j in range(n+1):
        colour[i].append([])
for i in range(1,m+1):
    s,e,c=map(int,raw_input().split())
    colour[c][s].append(e)
    colour[c][e].append(s)
q=input()
def dfs(s,e,c):
    global colour,done
    for i in range(len(colour[c][s])):
        if e==colour[c][s][i]:
            return 1
        if colour[c][s][i] not in done:
            done.append(colour[c][s][i])
            if dfs(colour[c][s][i],e,c)==1:
                return 1
    return 0
for i in range(q):
    ans=0
    s,e=map(int,raw_input().split())
    for j in range(1,m+1):
        done=[s]
        ans+=dfs(s,e,j)
    print ans