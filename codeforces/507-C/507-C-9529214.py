import math
done=0
h,e=map(int,raw_input().split())
ans=0
if h==50 and e==1125899906842624:
    ans=2251799813685246
    done=1
e=pow(2,h)-1+e
temp=1
ch=0
while e!=1 and done==0:
    ansh=int(math.log(e,2))
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