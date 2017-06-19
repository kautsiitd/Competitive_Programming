for _ in range(input()):
    s = raw_input()
    answer = 0
    last = "U"
    for c in s:
        if last != c:
            answer += 1
            last = c
    print (answer+1)/2
