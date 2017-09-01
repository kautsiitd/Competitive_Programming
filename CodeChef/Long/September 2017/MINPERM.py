for _ in range(input()):
    n = input()
    a = []
    if n%2 == 1:
        for i in range(1,n-3,2):
            a.append(i+1)
            a.append(i)
        a.append(n-1)
        a.append(n)
        a.append(n-2)
    else:
        for i in range(1,n,2):
            a.append(i+1)
            a.append(i)
    for i in a:
        print i,
    print ""
