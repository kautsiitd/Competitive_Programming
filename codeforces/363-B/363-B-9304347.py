n,k=map(int,raw_input().split())
a=map(int,raw_input().split())
tillmax=sum(a[:k])
ans=1
last=tillmax
for i in range(k,n):
    new=last+a[i]-a[i-k]
    if new<tillmax:
        tillmax=new
        ans=i-k+2
    last=new
print ans