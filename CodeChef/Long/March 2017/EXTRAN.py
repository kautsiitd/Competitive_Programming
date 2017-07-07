for _ in range(input()):
    n = input()
    a = sorted(map(int, raw_input().split()))
    found = False
    for i in range(1,n-2):
        if a[i+1] - a[i] != 1:
            found = True
            if a[i+2] - a[i+1] != 1:
                print a[i+1]
                break
            if a[i] - a[i-1] != 1:
                print a[i]
                break
    if not found:
        if a[1] - a[0] != 1:
            print a[0]
        else:
            print a[-1]
