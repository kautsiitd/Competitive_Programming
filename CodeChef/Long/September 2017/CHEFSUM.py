for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    b = min(a)
    for i in range(n):
        if b == a[i]:
            print i+1
            break
