import math

for _ in range(input()):
    n,v1,v2 = map(int,raw_input().split())
    t2 = 2.0/v2
    t1 = math.sqrt(2)/v1
    if t1<t2:
        print "Stairs"
    else:
        print "Elevator"
