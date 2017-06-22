for _ in range(input()):
    n,x = map(int, raw_input().split())
    a = map(int, raw_input().split())
    lowest = min(a)
    s = sum(a)
    if s%x != 0 and s/x == (s-lowest)/x:
        print -1
    else:
        print s/x
