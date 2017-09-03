for _ in range(input()):
    n = input()
    a = [[int(i) for i in raw_input()] for _ in range(n)]
    onePos = [(i+1,j+1) for i in range(n) for j in range(n) if a[i][j] == 1]
    print len(onePos)
    for point in onePos:
        print 0,1,0,1,0,1,point[1],point[0],point[0]
