n,m=map(int,raw_input().split())
a=map(int,raw_input().split())
a.sort()
diff=1000000
for i in range(n-1,m):
    if diff>a[i]-a[i-n+1]:
        diff=a[i]-a[i-n+1]
print diff