for _ in range(input()):
    a = raw_input()
    b = raw_input()
    l = len(a)
    answer = ""
    for i in range(l):
        if a[i] == b[i]:
            if a[i] == 'B':
                answer += 'W'
            else:
                answer += 'B'
        else:
            answer += 'B'
    print answer
