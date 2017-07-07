for _ in range(input()):
    s = raw_input()
    s = s.strip("=")
    if s == "":
        print 1
        continue
    lastSymbol = s[0]
    maxNumberOfSymbol = 0
    currentCount = 1
    for sign in s[1:]:
        if sign == "=":
            continue
        if sign == lastSymbol:
            currentCount +=1
        else:
            lastSymbol = sign
            maxNumberOfSymbol = max(maxNumberOfSymbol, currentCount)
            currentCount = 1

    maxNumberOfSymbol = max(maxNumberOfSymbol, currentCount)
    print maxNumberOfSymbol + 1
