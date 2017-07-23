for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    ans = 0
    for i in a:
        ans = ans | i
    print ans
