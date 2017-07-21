import random

t = 10
print t
for _ in range(t):
    n,m = random.randint(1,10),random.randint(0,10)
    print n,m
    s = "".join([str(random.randint(0,1)) for i in range(n)])
    print s
