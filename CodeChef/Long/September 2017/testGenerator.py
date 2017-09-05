import random
n,q = random.randint(200000,200000),random.randint(200000,200000)
print n,q
for i in range(n-1):
    print i,i+1
for _ in range(n):
    print random.randint(99999999999999990,1000000000000000000),
print ""
for i in range(q):
    print i
