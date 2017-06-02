def dist(cordA, cordB):
    dx = cordA[0] - cordB[0]
    dy = cordA[1] - cordB[1]
    dd = min(abs(dx), abs(dy))
    return dd + abs(abs(dx) - dd) + abs(abs(dy) - dd)

for _ in range(input()):
    n, m = map(int, raw_input().split())
    a = []
    maximum = -1
    for i in range(n):
        row = map(int, raw_input().split())
        maximum = max(max(row), maximum)
        a.append(row)

    maxCords = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == maximum:
                maxCords.append([j,i])

    answer1 = 10000
    answer2 = 10000
    answer3 = 10000
    answer4 = 10000
    for maxCord in maxCords:
        answer1 = min(answer1, dist([0,0], maxCord))
        answer2 = min(answer2, dist([0,n-1], maxCord))
        answer3 = min(answer3, dist([m-1,0], maxCord))
        answer4 = min(answer4, dist([m-1,n-1], maxCord))
    print max(answer1, answer2, answer3, answer4)
