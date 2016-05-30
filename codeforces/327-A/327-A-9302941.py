n=input()
a=map(int,raw_input().split())
b=[]
ans=0
for i in range(n):
    if a[i]==1:
        ans+=1
        b.append(-1)
    else:
        b.append(1)
maxtill=0
maxend=0
if ans==n:
    print ans-1
else:
    for i in range(n):
        maxend+=b[i]
        if maxend<0:
            maxend=0
        if maxend>maxtill:
            maxtill=maxend
    print maxtill+ans