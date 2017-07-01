for _ in range(input()):
    n = input()
    for i in range(1,100000):
        if (i*(i+1) > 2*n):
            print i-1
            break
