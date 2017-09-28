for _ in range(input()):
    s = raw_input()
    sMax = s.split('*')
    ansMax = 1
    for i in sMax:
        temp = map(int,i.split('+'))
        ansMax *= sum(temp)
    print ansMax

    sMin = s.split('+')
    ansMin = 0
    for i in sMin:
        temp = map(int,i.split('*'))
        tempAns = 1
        for j in temp:
            tempAns *= j
        ansMin += tempAns
    print ansMin
