n=input()
a=[0]*102
c=map(int,raw_input().split())
for i in range(n):
    a[c[i]]+=1
m=input()
b=[0]*102
d=map(int,raw_input().split())
for i in range(m):
    b[d[i]]+=1
ans=0
for i in range(1,101):
    if a[i]==0:
        continue
    ans+=min(a[i],b[i-1])
    temp=a[i]
    a[i]-=min(a[i],b[i-1])
    b[i-1]-=min(temp,b[i-1])
    ans+=min(a[i],b[i])
    temp=a[i]
    a[i]-=min(a[i],b[i])
    b[i]-=min(temp,b[i])
    ans+=min(a[i],b[i+1])
    temp=a[i]
    a[i]-=min(a[i],b[i+1])
    b[i+1]-=min(temp,b[i+1])
print ans