import random
t = 100
print t
upperLimitNum = 4
upperLimitN = 8
for _ in range(t):
    n = random.randint(1,upperLimitN)
    print n
    for __ in range(n):
        print random.randint(0,upperLimitNum),
    print ""
