for _ in range(input()):
    n = input()
    c = map(int,raw_input().split())
    w = map(int,raw_input().split())
    tempSum = 0
    wcum = [0]
    for i in range(n):
        tempSum += w[i]
        wcum.append(tempSum)

    i = 0
    j = 0
    d = {}
    answer = w[0]
    while j!=n:
        if c[j] in d:
            answer = max(answer, wcum[j]-wcum[i])
            while c[i] != c[j]:
                d.pop(c[i], None)
                i += 1
            i += 1
            answer = max(answer, wcum[j+1]-wcum[i])
        else:
            d[c[j]] = True
        j+=1
    answer = max(answer, wcum[j]-wcum[i])
    print answer
