n=input()
a=map(int,raw_input().split())
a.sort()
b=[0]*100001
for i in range(n):
    b[a[i]]+=1
f=[0]*100001
f[1]=b[1]
for i in range(2,100001):
    f[i]=max(f[i-1],f[i-2]+b[i]*i)
print f[100000]