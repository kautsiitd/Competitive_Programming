def printIt():
    for i in ans:
        print i[0]*a[0][i]
    print ""

def updateAns(i):
    for j in range(n):
        temp = []
        if a[0][j]

n,q = map(int,raw_input().split())
a = [map(int,raw_input().split()) for _ in range(n)]
ans = [[-1,1] for i in range(n)]
for i in range(1,n):
    updateAns(i)
printIt()
for _ in range(q):
    rowIndex = input()
    row = map(int,raw_input().split())
    a[rowIndex-1] = row
    for i in range(n):
        a[i][rowIndex-1] = row[i]
    updateAns(rowIndex-1)
    printIt()
