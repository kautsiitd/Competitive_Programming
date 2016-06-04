import math
r,x,y,a,b=map(int,raw_input().split())
d=math.sqrt(pow(x-a,2)+pow(y-b,2))
ans=d/(2*r)
if(int(ans)<ans):
    print int(ans)+1
else:
    print int(ans)