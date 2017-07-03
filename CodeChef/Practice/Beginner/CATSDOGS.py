for _ in range(input()):
    c,d,l = map(int,raw_input().split())
    flag=False
    if l%4 == 0:
        l /= 4
        if l >= d:
            l -= d
            if l <= c:
                if c-l <= 2*d:
                    flag = True
    if flag:
        print "yes"
    else:
        print "no"
