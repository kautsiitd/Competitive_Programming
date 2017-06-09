for _ in range(input()):
    n = input()
    a = map(int, raw_input().split())
    b = []
    c = []
    answer = 0
    for element in a:
        if element < 0:
            c.append(element)
        else:
            b.append(element)
    c.sort(reverse=True)
    bSum = sum(b)
    cSum = sum(c)
    cl = len(c)
    bl = len(b)
    answer = bl*bSum + cSum
    for index in range(cl):
        bl += 1
        bSum += c[index]
        cSum -= c[index]
        answer = max(answer, (bl*bSum) + cSum)
    print answer
