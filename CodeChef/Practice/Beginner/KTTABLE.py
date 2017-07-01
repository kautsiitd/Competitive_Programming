for _ in range(input()):
    n = input()
    a = [0]+map(int,raw_input().split())
    b = map(int,raw_input().split())
    print sum([1 for i in range(n) if a[i+1]-a[i]>=b[i]])
