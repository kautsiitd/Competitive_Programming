import random
t = 3
print t
for _ in range(t):
    n,m,k = 5000,10000,3
    print n,m,k
    dict = {(1,2):True}
    print 1,2
    for i in range(3,n+1):
        dict[(1,i)] = True
        dict[(i,i-1)] = True
        print 1,i
        print i,i-1
    for i in range(2*n-2,m+1):
        a,b = random.randint(1,n),random.randint(1,n)
        while(a==b or (a,b) in dict):
            a,b = random.randint(1,n),random.randint(1,n)
        dict[(a,b)] = True
        dict[(b,a)] = True
        print a,b
