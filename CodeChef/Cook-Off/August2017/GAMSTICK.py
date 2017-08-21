for _ in range(input()):
    n,x1,y1,x2,y2 = map(int,raw_input().split())
    if y1 == y2:
        print "Draw"
        continue
    if y1>y2:
        y1 = n-y1+1
        y2 = n-y2+1
    if x1 == x2:
        mid = (y2+y1)/2
        mCover = mid*2
        if mCover > n:
            print "Miron"
        elif mCover == n:
            print "Draw"
        else:
            print "Slava"
    else:
        mCover = ((y2-y1-1)/2 + y1)*2
        if mCover > n:
            print "Miron"
        elif mCover < n:
            if y2-y1 == 1:
                print "Draw"
            else:
                if mCover+2 >= n:
                    print "Draw"
                else:
                    print "Slava"
        else:
            print "Draw"
