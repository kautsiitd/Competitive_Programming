for _ in range(input()):
    s = raw_input()
    if len(s) < 2:
        print "NO"
        continue
    elif s[0] == s[1]:
        print "NO"
        continue
    index = 0
    answer = "YES"
    for c in s:
        if c == s[index]:
            index -= 1
            index = abs(index)
        else:
            answer = "NO"
            break
    print answer
