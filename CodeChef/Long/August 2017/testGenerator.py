import random
t = 5
print t
for _ in range(t):
    n,c = random.randint(1,3000),1
    b = random.randint(1,int(30000/n))
    # n = random.randint(1,upperLimitN)
    print n,b,c
    s = 1
    for __ in range(n):
        s += random.randint(1,100000)
        print s,
    print ""
