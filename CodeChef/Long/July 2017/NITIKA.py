for _ in range(input()):
    a = raw_input().split()
    answer = ""
    for i in range(len(a)-1):
        answer += a[i][0].upper() + ". "
    answer += a[-1][0].upper() + a[-1][1:].lower()
    print answer
