n=input()
a=[0]
a=a+map(int,raw_input().split())
last=0;i=2;current=1;ans=1;start=1
while i<=n:
    while i<=n and a[i]>a[i-1]:
        current+=1;i+=1
    if (last==1 or current==1 or last==0 or a[start+1]-a[start-1]>1 or a[start]-a[start-2]>1) and current+last>ans:
        ans=current+last
    elif (a[start+1]-a[start-1]<=1) and max(current+1,last+1)>ans:
        ans=max(current+1,last+1)
    last=current;start=i;current=1
    i+=1
if i==n+1:
    print max(last+1,ans)
else:
    print ans