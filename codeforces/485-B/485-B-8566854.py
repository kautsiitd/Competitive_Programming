n=input()
a1=[]
a2=[]
for i in range(n):
    x,y=map(int,raw_input().split())
    a1.append(x)
    a2.append(y)
print pow(max((max(a1)-min(a1)),(max(a2)-min(a2))),2)