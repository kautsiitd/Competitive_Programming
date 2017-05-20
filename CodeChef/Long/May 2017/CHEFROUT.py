allowed = ["CES", "CE", "CS", "ES", "C", "E", "S"]
for i in range(input()):
    s = raw_input()
    newS = ""
    lastC = ""
    for c in s:
        if c != lastC:
            newS += c
            lastC = c
    answer = "no"
    for correct in allowed:
        if newS == correct:
            answer = "yes"
            break
    print answer
