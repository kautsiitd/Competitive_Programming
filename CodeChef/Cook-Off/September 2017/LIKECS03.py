for _ in range(input()):
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    elementsNeeded = [pow(2,i) for i in range(k)]
    ans = 0
    for i in elementsNeeded:
        if not(i in a):
            ans += 1
    print ans
