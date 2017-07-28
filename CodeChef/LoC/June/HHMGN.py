for _ in range(input()):
    n,s = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()
    aCum = [0]
    [aCum.append(aCum[i] + a[i]) for i in range(n)]

    answer = -1
    if aCum[-1] < s:
        answer = -1
    elif aCum[-1] == s:
        answer = a[-1]
    else:
        for i in range(1,n):
            if (s-aCum[i])%(n-i) == 0 and (s-aCum[i])/(n-i) >= a[i-1] and aCum[i] + ((s-aCum[i])/(n-i)*(n-i)) == s:
                answer = (s-aCum[i])/(n-i)
    print answer
