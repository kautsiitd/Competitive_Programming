n=input()
a=[]
b=[]
c=[]
t=map(int,raw_input().split())
for i in range(n):
    if t[i]==1:
        a.append(i+1)
    elif t[i]==2:
        b.append(i+1)
    else:
        c.append(i+1)
x=min(len(a),min(len(b),len(c)))
print x
for i in range(x):
    print a[i],b[i],c[i]