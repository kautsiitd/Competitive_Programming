n=input()
a=map(int,raw_input().split())
sa=[0]
current=0
for i in range(n):
    current+=a[i]
    sa.append(current)
a.sort()
sb=[0]
current=0
for i in range(n):
    current+=a[i]
    sb.append(current)
m=input()
for i in range(m):
    t,l,r=map(int,raw_input().split())
    if t==1:
        print sa[r]-sa[l-1]
    else:
        print sb[r]-sb[l-1]