for _ in range(input()):
    n = input()
    l = map(int,raw_input().split())
    r = map(int,raw_input().split())
    maxScore = max([l[i]*r[i] for i in range(n)])
    maxRating = max([r[i] for i in range(n) if l[i]*r[i]==maxScore])

    for i in range(n):
        if l[i]*r[i] == maxScore and r[i] == maxRating:
            print i+1
            break
