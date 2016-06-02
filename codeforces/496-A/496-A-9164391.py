n=input()
a=map(int,raw_input().split())
currentmax=-1
for i in range(1,n):
    if currentmax==-1 or currentmax<a[i]-a[i-1]:
        currentmax=a[i]-a[i-1]
ans=[]
for i in range(1,n-1):
    ans.append(max(a[i+1]-a[i-1],currentmax))
print min(ans)