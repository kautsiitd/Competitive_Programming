import sys
def f(i):
    return -i+offset
n = 5
a = [[0 for j in range(n)] for i in range(n)]
b = [(5,1,4)]
for offset,l,r in b:
    for i in range(l-1,r):
        if f(i) < n and f(i) >= 0:
            a[i][f(i)] = 1
for i in a:
    for j in i:
        print j,
    print ""
