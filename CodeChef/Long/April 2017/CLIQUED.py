import heapq as hq


def djik(graph,s,n):
    dist={}
    vis=[False]*(n+2)
    for i in range(1,n+2):
        dist[i]=float('inf')
    dist[s]=0
    #vis[s]=True
    h=[]
    hq.heappush(h,(0,s))
    #for i in graph[s]:
    #    hq.heappush(h,i)
    #print h
    while not len(h)==0:
        #print h,
        a=hq.heappop(h)
        #print a
        if vis[int(a[1])]==True:
            #pass
            continue
        ###print a
        u=a[1]
        d=a[0]
        for j in graph[u]:
            i=j[1]
            w=j[0]
            if dist[i]>dist[u]+w:
                dist[i]=dist[u]+w
                hq.heappush(h,(dist[i],i))
        vis[u]=True
    return dist

t= int(raw_input())
while t:
    t=t-1
    n,k,x,m,s=map(int,raw_input().split())
    graph={}
    for i in range(1,n+2):
        graph[i]=[]
    for i in range(1,k+1):
        graph[i].append((float(x)/2,n+1))
        graph[n+1].append((float(x)/2,i))
    while m:
        m=m-1
        a,b,c=map(int,raw_input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))
    #print graph
    d= djik(graph,s,n)
    for i in d:
        if i!=n+1:
            print int(d[i]),
    print ""
