for _ in range(input()):
    input()
    a = map(int,raw_input().split())
    nGreater = 0
    for i in a:
        if i>1:
            nGreater += 1
    if nGreater > 1:
        print "no"
    else:
        print "yes"
