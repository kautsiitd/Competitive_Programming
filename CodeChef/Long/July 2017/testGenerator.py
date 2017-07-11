import random
t = 5
print t
for _ in range(t):
    n = 10000
    print n
    for i in range(n-1):
        print i+1,i+2,i+1

    q = 100000
    print q
    for i in range(q):
        a = random.randint(1,n-1)
        b = random.randint(a+1,n)
        print a,b,random.randint(1,1000000000)
