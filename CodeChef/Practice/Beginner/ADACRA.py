def findAnswer(last):
    answer = 0
    for c in s:
        if last != c:
            answer += 1
            last = c
    return (answer+1)/2

for _ in range(input()):
    s = raw_input()
    print min(findAnswer("U"), findAnswer("D"))
