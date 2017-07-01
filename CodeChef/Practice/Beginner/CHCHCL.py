for _ in range(input()):
    n,m = map(int, raw_input().split())
    print ["Yes","No"][n*m%2]
