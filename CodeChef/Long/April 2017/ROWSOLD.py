for i in range(input()):
    s = raw_input()
    oneCount = 0
    zeroCount = 0
    answer = 0
    for j in s:
        if j == '1':
            if zeroCount !=0:
                answer += (oneCount * (zeroCount + 1))
                zeroCount = 0
            oneCount += 1
        else:
            zeroCount += 1
    if zeroCount !=0:
        answer += (oneCount * (zeroCount + 1))
        zeroCount = 0
    print answer
