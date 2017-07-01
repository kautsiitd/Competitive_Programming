for _ in range(input()):
    n = input()
    a = map(int, raw_input().split())
    xor = 0
    for i in a:
        xor ^= i
    print a.count(xor)
