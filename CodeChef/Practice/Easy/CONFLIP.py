for _ in range(input()):
    for __ in range(input()):
        i,n,q = map(int,raw_input().split())
        if i == q:
            print n/2
        else:
            print (n+1)/2
