for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    b = map(int,raw_input().split())
    score1 = sum([a[i] for i in range(n) if i%2 == 0]) + sum([b[i] for i in range(n) if i%2 == 1])
    score2 = sum([b[i] for i in range(n) if i%2 == 0]) + sum([a[i] for i in range(n) if i%2 == 1])
    print min(score1, score2)
