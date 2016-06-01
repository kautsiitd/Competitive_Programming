import math
n=input()
for i in range(n):
    l,r=map(int,raw_input().split())
    if l==r:
        print l
        continue
    if l==0:
        templ=0
    else:
        templ=int(math.log(l,2))+1
    tempr=int(math.log(r,2))+1
    ql=int(math.log(l+1,2))
    qr=int(math.log(r+1,2))
    #print ql,qr
    #print tempr,templ
    if ql!=qr or pow(2,qr)==r+1:
        print pow(2,qr)-1
        continue
    elif templ!=tempr:
        print pow(2,tempr-1)-1
        continue
    oldx=bin(l)
    oldy=bin(r)
    x=bin(l)
    y=bin(r)
    #print x,y
    ans=0
    while x[2]==y[2]:
        x=x[0:2]+x[3:]
        y=y[0:2]+y[3:]
        ans+=1
    newl=int(x,2)
    newr=int(y,2)
    temp=int(math.log(max(newl,newr)+1,2))
    kanu=oldx[:ans+2]
    #print kanu,x,ans
    #print ans+2,tempr-temp,tempr,temp
    for i in range(tempr-temp-ans):
        kanu+='0'
    for i in range(temp):
        kanu+='1'
    #print kanu
    print int(kanu,2)