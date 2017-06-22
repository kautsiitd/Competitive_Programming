for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    k = input()
    match = a[k-1]
    a.sort()
    print a.index(match) + 1
