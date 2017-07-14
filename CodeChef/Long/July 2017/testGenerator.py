import random
import math
t = 100000
print t
a = [2,311,13,17,19,23,29]
for i in range(31,2480,2):
    isPrime = True
    upperLimit = int(math.sqrt(i))+2
    for j in a:
        if j>upperLimit:
            break
        elif i%j == 0:
            isPrime = False
            break
    if isPrime:
        a.append(i)
l = len(a)
for _ in range(t):
    n = 3
    print n
    a1 = random.randint(0,l-3)
    a2 = random.randint(a1+1,l-2)
    a3 = random.randint(a2+1,l-1)
    print a[a1],a[a2],a[a3]
