t = 100
print t
for _ in range(t):
    n = 10000
    print n
    b = [(i+2)*2 for i in range((n-2)/2)]
    c = [(i*2)+3 for i in range((n-2)/2)][::-1]
    a = [1]+b+c+[2]
    for i in a:
        print i,
    print ""
