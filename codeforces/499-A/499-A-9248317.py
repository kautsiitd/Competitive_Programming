n,x=map(int,raw_input().split())
a=[]
for z in range(n):
    s,e=map(int,raw_input().split())
    a.append([s,e])
l=0
ans=0
while l!=n:
    ans+=a[l][1]-a[l][0]+1
    l+=1
current=1
l=0
while l<n:
    if current<a[l][0] and current+x<a[l][0]:
        current+=x
    elif current<a[l][0] and current+x>a[l][0]:
        ans+=a[l][0]-current
        current=a[l][1]+1
        l+=1
    elif current<a[l][0] and current+x==a[l][0]:
        current=a[l][1]+1
        l+=1
    elif current==a[l][0]:
        current=a[l][1]+1
        l+=1
print ans