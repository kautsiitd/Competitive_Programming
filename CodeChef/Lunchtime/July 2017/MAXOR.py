for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if (a[i] | a[j]) <= max(a[i],a[j]):
                ans += 1
    print ans
    # binMat = []
    # for i in a:
    #     bitArray = []
    #     temp = i
    #     for j in range(2):
    #         bitArray.append(i%2)
    #         i/=2
    #     binMat.append(bitArray[::-1])
    # print binMat
