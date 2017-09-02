import random
t = 10
print t
for _ in range(t):
    n,q = random.randint(2,100000),random.randint(1,100000)
    print n,q
    for _ in range(q):
        print random.randint(2,n),random.randint(2,n),random.randint(0,1)
