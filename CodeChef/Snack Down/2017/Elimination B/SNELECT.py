for _ in range(input()):
    s = raw_input()
    l = len(s)
    for i in range(l):
        if s[i] == "s" and i > 0 and s[i-1] == "m":
            s = s[:i-1] + "#." + s[i+1:]
        elif s[i] == "s" and i < l-1 and s[i+1] == "m":
            s = s[:i] + ".#" + s[i+2:]

    answer = 0
    for c in s:
        if c == "s":
            answer -= 1
        elif c == "m" or c == "#":
            answer += 1
    if answer < 0:
        print "snakes"
    elif answer == 0:
        print "tie"
    else:
        print "mongooses"
