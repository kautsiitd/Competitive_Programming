for _ in range(input()):
    input()
    a = map(int,raw_input().split())
    count = 0
    for i in a:
        while i%2 == 0:
            i /= 2
            count += 1
    if count%2 == 0:
        print "Alan"
    else:
        print "Charlie"
