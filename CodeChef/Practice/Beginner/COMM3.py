import math
for _ in range(input()):
    maxd = input()
    a1,a2 = map(int,raw_input().split())
    b1,b2 = map(int,raw_input().split())
    c1,c2 = map(int,raw_input().split())
    answer = 0
    if (math.sqrt((b1-a1)*(b1-a1) + (b2-a2)*(b2-a2)) <= maxd):
        answer += 1
    if (math.sqrt((c1-a1)*(c1-a1) + (c2-a2)*(c2-a2)) <= maxd):
        answer += 1
    if (math.sqrt((b1-c1)*(b1-c1) + (b2-c2)*(b2-c2)) <= maxd):
        answer += 1

    if answer >= 2:
        print "yes"
    else:
        print "no"
