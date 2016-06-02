m1,m2=map(int,raw_input().split())
u1,u2=map(int,raw_input().split())
n=input()
ans=0
for i in range(n):
    a,b,c=map(int,raw_input().split())
    if (a*m1+b*m2+c)*(a*u1+b*u2+c)<0:
        ans+=1
print ans