for _ in range(input()):
    s = raw_input()
    l = len(s)
    costMap = {}
    costMap[s[0]] = 0
    for i in range(1,l):
        if not(s[i] in costMap):
            costMap[s[i]] = costMap[s[i-1]] + abs(ord(s[i])-ord(s[i-1]))
        else:
            costMap[s[i]] = min(costMap[s[i]], costMap[s[i-1]] + abs(ord(s[i])-ord(s[i-1])))

    print costMap[s[-1]]
