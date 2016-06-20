n=input()
a=[[1]]
for i in range(n-1):
    a[0].append(1)
for j in range(n-1):
    a.append([1])
for i in range(1,n):
    for j in range(1,n):
        a[i].append(a[i-1][j]+a[i][j-1])
print a[n-1][n-1]