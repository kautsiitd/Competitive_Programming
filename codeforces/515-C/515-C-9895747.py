n=input()
d=raw_input()
a=[]
for i in range(n):
    if(d[i]=='2'):
        a.append(2)
    elif(d[i]=='3'):
        a.append(3)
    elif(d[i]=='4'):
        a.append(3)
        a.append(2)
        a.append(2)
    elif(d[i]=='5'):
        a.append(5)
    elif(d[i]=='6'):
        a.append(5)
        a.append(3)
    elif(d[i]=='7'):
        a.append(7)
    elif(d[i]=='8'):
        a.append(7)
        a.append(2)
        a.append(2)
        a.append(2)
    elif(d[i]=='9'):
        a.append(7)
        a.append(3)
        a.append(3)
        a.append(2)
a.sort()
ans=0
l=len(a)
last=1
for i in range(len(a)):
    ans+=last*a[i]
    last*=10
print ans