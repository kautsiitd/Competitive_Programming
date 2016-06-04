import math
h,e=map(int,raw_input().split())
ans=0
e=pow(2,h)-1+e
a=[1]
temp=1
for i in range(1,52):
    temp*=2
    a.append(temp)
while e!=1:
    i=0
    while(e>=a[i]):
        i+=1
    ansh=i-1
    if (e/2)%2==0:
        if e%2==1:
            ans+=1
        else:
            ans+=pow(2,h-ansh+1)
    else:
        if e%2==0:
            ans+=1
        else:
            ans+=pow(2,h-ansh+1)
    e/=2
print ans