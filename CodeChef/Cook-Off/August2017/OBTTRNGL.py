for _ in range(input()):
    n,a,b = map(int,raw_input().split())
    diff = abs(b-a)
    if n%2 == 0 and diff == n/2:
        print 0
    else:
        print min(abs(a-b)-1,n-abs(a-b)-1)
