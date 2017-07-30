import random
t = 5
print t

for _ in range(t):
    n = random.randint(1,1000)
    m = random.randint(1,min(n,100))
    print n,m
    upperLimit = 100000
    for i in range(n):
        a = random.randint(0,upperLimit)
        b = random.randint(a,upperLimit)
        print a,b

    kSize = 60
    k = "1"
    for i in range(1,kSize):
        k += str(random.randint(0,1))
    print k
