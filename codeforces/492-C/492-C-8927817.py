n,m,avg=map(int,raw_input().split())
cavg=0
a=[]
ans=0
for i in range(n):
    a.append(map(int,raw_input().split()))
a.sort(key=lambda x:x[1])
for i in range(n):
    cavg+=a[i][0]
if cavg>=avg*n:
    print 0
else:
    r=avg*n-cavg
    i=0
    while r>0:
        if a[i][0]<m:
            temp=m-a[i][0]
            if temp-r>=1:
                if r/1==r:
                    ans+=int(r)*a[i][1]
                else:
                    ans+=(int(r)+1)*a[i][1]
                r=0
            else:
                r-=(m-a[i][0])
                ans+=(m-a[i][0])*a[i][1]
        i+=1
    print ans