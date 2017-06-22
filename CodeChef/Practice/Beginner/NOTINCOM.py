for _ in range(input()):
    n1,n2 = map(int, raw_input().split())
    a = map(int,raw_input().split())
    b = map(int,raw_input().split())
    c = [False for i in range(1000005)]
    for i in a:
        c[i] = True
    answer = 0
    for i in b:
        if c[i] == True:
            answer += 1
    print answer
