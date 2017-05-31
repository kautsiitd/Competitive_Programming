for i in range(input()):
    n, t = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()
    for j in range(t):
        limit = input()
        rightStart = n-1
        leftStart = 0
        extra = 0
        answer = 0
        while rightStart >= leftStart:
            if a[rightStart] + extra >= limit:
                rightStart -= 1
                answer += 1
            else:
                extra += 1
                leftStart += 1
        print answer
