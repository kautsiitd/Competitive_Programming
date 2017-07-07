import random
t = 1000
print t
for _ in range(t):
    n = random.randint(4,1000)
    b = random.randint(1,n/4)
    print n,b
