for _ in range(input()):
    n,m,o = map(int, raw_input().split())
    a = sorted(map(int, raw_input().split()))
    b = sorted(map(int, raw_input().split()))
    c = sorted(map(int, raw_input().split()))
    mod = 1000000007

    aCum = [0]
    for element in a:
        aCum.append((aCum[-1] + element)%mod)
    cCum = [0]
    for element in c:
        cCum.append((cCum[-1] + element)%mod)

    def findPos(num, name):
        lower = 0
        if name == "a":
            array = a
            upper = n
        else:
            array = c
            upper = o
        mid = (lower+upper)/2

        while lower<upper:
            mid = (lower+upper)/2
            if array[mid] > num:
                upper = mid
            else:
                lower = mid + 1
        return lower

    answer = 0
    for d in b:
        aIndex = findPos(d, "a")
        cIndex = findPos(d, "c")
        answer += ((aCum[aIndex] + ((aIndex*d)%mod))%mod) * ((cCum[cIndex] + ((cIndex*d)%mod))%mod)
        answer%=mod
    print answer
