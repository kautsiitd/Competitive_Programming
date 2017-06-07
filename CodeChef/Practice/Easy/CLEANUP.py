for _ in range(input()):
    n,m = map(int, raw_input().split())
    a = sorted(map(int, raw_input().split()))
    b = []; c = []
    pointer = 0
    index = 0
    for i in range(1,n+1):
        if index < m and i == a[index]:
            index += 1
            continue
        else:
            if pointer == 0:
                b.append(i)
            else:
                c.append(i)
            pointer = abs(pointer - 1)
    for i in range(len(b)-1):
        print b[i],
    if len(b) > 0:
        print b[-1]
    else:
        print ""
    for i in range(len(c)-1):
        print c[i],
    if len(c) > 0:
        print c[-1]
    else:
        print ""
