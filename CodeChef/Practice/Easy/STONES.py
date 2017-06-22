for _ in range(input()):
    j = raw_input()
    s = raw_input()
    answer = 0
    for c in s:
        if c in j:
            answer += 1
    print answer
