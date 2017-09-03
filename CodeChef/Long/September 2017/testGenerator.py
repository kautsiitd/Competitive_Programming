import random
n,q = random.randint(4900,5000),random.randint(199999,200000)
print n,q
for i in range(n-1):
    print i,i+1
for _ in range(n):
    print random.randint(999999999999999990,1000000000000000000),
print ""
for _ in range(q):
    print random.randint(0,1000000000000000000)
