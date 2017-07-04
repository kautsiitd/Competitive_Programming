for _ in range(input()):
    n,b,m = map(int,raw_input().split())
    answer = 0
    factor = m
    while n > 1:
        answer += factor*([n/2, (n+1)/2][n%2]) + b
        factor *= 2
        n /= 2
    answer += factor*n
    if n == 0:
        answer -= b
    print answer
