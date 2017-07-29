import math

for _ in range(input()):
    n,m = map(int,raw_input().split())
    if n*(n+1)/2 < m :
        print -1
    else:
        a,b,c = 1,1,-2*m
        d = math.sqrt(1 - 4*a*c)
        ans = int((-b+d)/2)
        for i in range(max(ans-10,0),ans+10):
            if i*(i+1)/2 >= m:
                ans = i
                break
        print ans
