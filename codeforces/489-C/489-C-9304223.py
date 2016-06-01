m,s=map(int,raw_input().split())
if s==0:
    if m==1:
        print "0 0"
    else:
        print "-1 -1"
else:
    a=[0]*m;b=[0]*m
    a[0]=1;b[0]=1
    s1=s-1
    if s>9*m:
        print "-1 -1"
    else:
        current=m-1
        s-=1
        while s>0:
            if s>=9-a[current]:
                s-=9-a[current]
                a[current]=9
                current-=1
            else:
                a[current]+=s
                s=0
        current=0
        while s1>0:
            if s1>=9-b[current]:
                s1-=9-b[current]
                b[current]=9
                current+=1
            else:
                b[current]+=s1
                s1=0
        mi=""
        ma=""
        for i in range(m):
            mi+=str(a[i])
            ma+=str(b[i])
        print mi
        print ma