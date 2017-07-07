for _ in range(input()):
    n = input()
    numberOfZeros = sum([map(int,raw_input().split()).count(0) for __ in range(n)])
    bandwidth = n-1
    for i in range(1,n):
        if numberOfZeros < i*(i+1):
            break
        else:
            numberOfZeros -= i*(i+1)
            bandwidth -= 1

    print max(0,bandwidth)
