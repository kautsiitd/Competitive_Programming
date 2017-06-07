for _ in range(input()):
    s = raw_input()
    if len(s1) < 2:
        print "NO"
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
