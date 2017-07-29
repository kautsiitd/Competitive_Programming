import random

t = 100
print t
for __ in range(t):
    n = random.randint(1,50)
    pos = random.randint(0,n)
    for _ in range(n+1):
        if _ == pos:
            print n,
        else:
            print random.randint(1,100000),
    print ""
