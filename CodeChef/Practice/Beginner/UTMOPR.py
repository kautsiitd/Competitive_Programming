for _ in range(input()):
    n,k = map(int,raw_input().split())
    s = sum(map(int,raw_input().split()))
    if k == 1:
        print ["odd","even"][s%2]
    else:
        print "even"
