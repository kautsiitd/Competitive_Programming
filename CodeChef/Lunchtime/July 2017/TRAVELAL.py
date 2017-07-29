from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V= vertices
        self.graph = []
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
    def KruskalMST(self):
        global bestEdges
        result =[]
        i = 0
        e = 0
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        parent = [] ; rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V -1 :
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
            if x != y:
                e = e + 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)
        for u,v,weight in result:
            bestEdges.append(weight)

def findDis(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for _ in range(input()):
    n = input()
    a = [map(int,raw_input().split()) for i in range(n)]
    g = Graph(n)
    for i in range(n):
        for j in range(i+1,n):
            g.addEdge(i,j,-findDis(a[i],a[j]))

    bestEdges = []
    g.KruskalMST()
    print -max(bestEdges)
