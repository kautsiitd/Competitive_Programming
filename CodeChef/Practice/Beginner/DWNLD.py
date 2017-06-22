for _ in range(input()):
    n,k = map(int, raw_input().split())
    answer = 0
    for __ in range(n):
        t,d = map(int,raw_input().split())
        if k<t:
            answer += d*(t-k)
            k = 0
        else:
            k -= t
    print answer
