a,b=map(int,raw_input().split())
x=map(int,raw_input().split())
x.sort()
ans=-1
for i in range(a-1):
    if ans==-1 or ans<abs(x[i]-x[i+1]):
        ans=abs(x[i]-x[i+1])
print max(ans/2.0,x[0],b-x[a-1])