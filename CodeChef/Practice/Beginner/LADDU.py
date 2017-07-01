for i in range(input()):
    n,k = raw_input().split()
    n = int(n)

    answer = 0
    for g in range(n):
        s=raw_input()
        if s[:11] == "CONTEST_WON":
            if int(s[12:]) <= 20:
                answer += 300 + 20 - int(s[12:])
            else:
                answer = answer + 300
        elif s == "TOP_CONTRIBUTOR":
            answer = answer + 300
        elif s == "CONTEST_HOSTED":
            answer = answer + 50
        elif s[:9] == "BUG_FOUND":
            answer = answer + int(s[10:])

    if k == "INDIAN":
        print (int(answer/200))
    elif k == "NON_INDIAN":
        print (int(answer/400))
