for _ in range(input()):
    n,d = map(int,raw_input().split())
    a = map(int,raw_input().split())
    b = [[] for i in range(d)]

    for i in range(d):
        j = i
        while j<n:
            b[i].append(a[j])
            j+=d

    ans = 0
    c = []
    for i in range(len(b)):
        s = sum(b[i])
        l = len(b[i])
        if s%l != 0:
            ans = -1
            break
        c.append(s/l)

    for i in range(1,len(c)):
        if c[i] != c[i-1]:
            ans = -1
            break

    if ans != -1:
        for i in range(len(b)):
            deficient = 0
            haveMore = 0
            l = len(b[i])
            while deficient<l:
                while deficient<l and b[i][deficient] >= c[i]:
                    deficient += 1
                if deficient == l:
                    break
                while haveMore<n and b[i][haveMore] <= c[i]:
                    haveMore += 1
                if haveMore == l:
                    break
                transfer = min(c[i]-b[i][deficient],b[i][haveMore]-c[i])
                ans += transfer*abs(haveMore-deficient)
                b[i][deficient] += transfer
                b[i][haveMore] -= transfer
    print ans
