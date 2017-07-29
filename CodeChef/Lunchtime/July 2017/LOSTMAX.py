for _ in range(input()):
    a = sorted(map(int,raw_input().split()))
    l = len(a) - 1
    if a == [0]:
        print 0
    elif l == a[-1]:
        print a[-2]
    else:
        print a[-1]
