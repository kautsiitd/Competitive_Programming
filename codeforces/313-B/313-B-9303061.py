a=raw_input()
ans=[0]
temp=0
last=a[0]
for i in range(1,len(a)):
    if a[i]==last:
        ans.append(ans[i-1]+1)
    else:
        ans.append(ans[i-1])
    last=a[i]
m=input()
for i in range(m):
    s,e=map(int,raw_input().split())
    print ans[e-1]-ans[s-1]