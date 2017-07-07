for _ in range(input()):
    n = input()
    a = sorted(map(int, raw_input().split()))
    if a[1] - a[0] != 1:
        print a[0]
    elif a[-1] - a[-2] != 1:
        print a[-1]
    else:
        for i in range(n-1):
            if a[i] == a[i+1]:
                print a[i]
                break
