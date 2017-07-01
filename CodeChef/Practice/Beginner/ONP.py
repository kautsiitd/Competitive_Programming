for _ in range(input()):
    s = raw_input()
    answer = ""
    symbolStack = []
    for c in s:
        if c == ")":
            answer += symbolStack[-1]
            symbolStack.pop()
        elif c in "+-*/^":
            symbolStack.append(c)
        elif c != "(":
            answer += c
    print answer
