for _ in range(input()):
    n = input()
    print n
    a = [[i+1, i+2] for i in range(n-1)]
    a.append([n,1])
    for i in range(n):
        print n
        for j in range(n):
            print j+1,a[(i+j)%n][0],a[(i+j)%n][1]
