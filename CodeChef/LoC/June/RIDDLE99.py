for _ in range(input()):
    a,b,m = map(int, raw_input().split())
    if a%m == 0:
        print (b/m) - (a/m) + 1
    else:
        print (b/m) - (a/m)
