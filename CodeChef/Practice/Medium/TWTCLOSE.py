n,k = map(int, raw_input().split())
d = {}
answer = 0
for _ in range(k):
    s = raw_input()
    if s == "CLOSEALL":
        answer = 0
        d = {}
    else:
        number = s.split()[1]
        if number in d and d[number] == True:
            answer -= 1
            d[number] = False
        else:
            answer += 1
            d[number] = True
    print answer
