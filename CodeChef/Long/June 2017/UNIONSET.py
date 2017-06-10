for _ in range(input()):
    n,k = map(int, raw_input().split())
    sets = [[0 for j in range(k)] for i in range(n)]

    for row in range(n):
        a = map(int, raw_input().split())
        for column in a[1:]:
            sets[row][column - 1] = 1

    allPairs = [[0 for j in range(n)] for i in range(n)]
    for column in range(k):
        excludePairs = []
        for row in range(n):
            if sets[row][column] == 0:
                excludePairs.append(row)
        l = len(excludePairs)
        for i in range(l):
            for j in range(i+1,l):
                allPairs[excludePairs[i]][excludePairs[j]] = 1

    answer = 0
    for row in range(n):
        for column in range(row+1,n):
            if allPairs[row][column] == 0:
                answer += 1
    print answer
