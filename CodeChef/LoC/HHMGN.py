for _ in range(input()):
    n,s = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()
    aCum = []
    for i in range(n):
