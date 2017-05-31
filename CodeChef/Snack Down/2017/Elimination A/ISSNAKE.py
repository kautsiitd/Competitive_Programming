def checkOk(array):
    answer = True
    for x in array:
        for y in array[x]:
            if array[x][y] == "#":
                answer = False
                return answer
    return answer

for _ in range(input()):
    n = input()
    rowA = raw_input()
    rowB = raw_input()
    array = []
    for c in rowA:
        if c == ".":
            array.append([0])
        else:
            array.append([1])
    for i in range(n):
        c = rowB[i]
        if c == ".":
            array[i].append([0])
        else:
            array[i].append([1])
    x = 0
    y = 0
    asnwer = "no"

    tempArray = array
    isDone = False
    while x < n and tempArray[x][y] == 0:
        x += 1
    if x < n:
        while x < n and not isDone:
            tempArray[x][y] = 0
            if y == 0:
                if tempArray[x][y+1] == 1:
                    y += 1
                    continue
                elif x+1 < n and tempArray[x+1][y] == 1:
                    x += 1
                    continue
                else:
                    isDone = True
                    break
            if y == 1:
                if tempArray[x][y-1] == 1:
                    y -= 1
                    continue
                elif x+1 < n and tempArray[x+1][y] == 1:
                    x += 1
                    continue
                else:
                    isDone = True
                    break
        if checkOk(tempArray):
            answer == "yes"

    x = 0
    y = 1
    tempArray = array
    isDone = False
    while x < n and tempArray[x][y] == 0:
        x += 1
    if asnwer != "yes" and x < n:
        while x < n and not isDone:
            tempArray[x][y] = 0
            if y == 0:
                if tempArray[x][y+1] == 1:
                    y += 1
                    continue
                elif x+1 < n and tempArray[x+1][y] == 1:
                    x += 1
                    continue
                else:
                    isDone = True
                    break
            if y == 1:
                if tempArray[x][y-1] == 1:
                    y -= 1
                    continue
                elif x+1 < n and tempArray[x+1][y] == 1:
                    x += 1
                    continue
                else:
                    isDone = True
                    break
        if checkOk(tempArray):
            answer == "yes"

            x = 0
            y = 1
            tempArray = array
            isDone = False
            while x < n and tempArray[x][y] == 0:
                x += 1
            if asnwer != "yes" and x < n:
                while x < n and not isDone:
                    tempArray[x][y] = 0
                    if y == 0:
                        if tempArray[x][y+1] == 1:
                            y += 1
                            continue
                        elif x+1 < n and tempArray[x+1][y] == 1:
                            x += 1
                            continue
                        else:
                            isDone = True
                            break
                    if y == 1:
                        if tempArray[x][y-1] == 1:
                            y -= 1
                            continue
                        elif x+1 < n and tempArray[x+1][y] == 1:
                            x += 1
                            continue
                        else:
                            isDone = True
                            break
                if checkOk(tempArray):
                    answer == "yes"

    x = n-1
    y = 0
    tempArray = array
    isDone = False
    while x >= 0 and tempArray[x][y] == 0:
        x -= 1
    if asnwer != "yes" and x >= 0:
        while x < n and not isDone:
            tempArray[x][y] = 0
            if y == 0:
                if tempArray[x][y+1] == 1:
                    y += 1
                    continue
                elif x-1 >= 0 and tempArray[x-1][y] == 1:
                    x -= 1
                    continue
                else:
                    isDone = True
                    break
            if y == 1:
                if tempArray[x][y-1] == 1:
                    y -= 1
                    continue
                elif x-1 >= 0 and tempArray[x-1][y] == 1:
                    x -= 1
                    continue
                else:
                    isDone = True
                    break
        if checkOk(tempArray):
            answer == "yes"

    x = n-1
    y = 1
    tempArray = array
    isDone = False
    while x >= 0 and tempArray[x][y] == 0:
        x -= 1
    if asnwer != "yes" and x >= 0:
        while x < n and not isDone:
            tempArray[x][y] = 0
            if y == 0:
                if tempArray[x][y+1] == 1:
                    y += 1
                    continue
                elif x-1 >= 0 and tempArray[x-1][y] == 1:
                    x -= 1
                    continue
                else:
                    isDone = True
                    break
            if y == 1:
                if tempArray[x][y-1] == 1:
                    y -= 1
                    continue
                elif x-1 >= 0 and tempArray[x-1][y] == 1:
                    x -= 1
                    continue
                else:
                    isDone = True
                    break
        if checkOk(tempArray):
            answer == "yes"

    print answer
