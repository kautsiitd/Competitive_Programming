s = raw_input()
for _ in range(input()):
    t = raw_input()
    answer = "Yes"
    for c in t:
        if c not in s:
            answer = "No"
            break
    print answer
