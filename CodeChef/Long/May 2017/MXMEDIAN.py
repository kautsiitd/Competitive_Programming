for i in range(input()):
    n = input()
    a = map(int, raw_input().split())
    a.sort()
    b = a[:n]
    c = a[n:]
    print c[n/2]
    for i in range(n):
        if i == n-1:
            print str(b[i]) + " " + str(c[i])
        else:
            print str(b[i]) + " " + str(c[i]),
