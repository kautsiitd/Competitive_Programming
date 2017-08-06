for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    b = [a[0]]
    c = [[a[0],1]]
    for i in range(1,n):
        if a[i] != a[i-1]:
            b.append(a[i])
            c.append([a[i],1])
        else:
            c[-1][1] += 1

    frqCheck = True
    for i in range(len(c)/2):
        if c[i][1] != c[-i-1][1]:
            frqCheck = False
            break

    if b == [1,2,3,4,5,6,7,6,5,4,3,2,1] and frqCheck:
        print "yes"
    else:
        print "no"
