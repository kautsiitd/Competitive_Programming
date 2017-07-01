for _ in range(input()):
    n,m,k = map(int,raw_input().split())
    print max(0,abs(n-m)-k)
