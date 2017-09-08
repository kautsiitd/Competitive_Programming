import sys
def f(a,b,c,d,x):
    return a*x*x*x + b*x*x + c*x + d
n = 8
print n
arr = [[0 for j in range(n)] for i in range(n)]
a,b,c,d = 0,0,0,0
for a in range(0,1):
    for b in range(0,1):
        for c in range(2,3):
            for d in range(-n-1,n+1):
                for x in range(1,n+1):
                    if f(a,b,c,d,x)<=n and f(a,b,c,d,x) > 0:
                        arr[x-1][f(a,b,c,d,x)-1] = 1
for i in arr:
    for j in i:
        print j,
    print ""
