for _ in range(input()):
    n = input()
    a = map(int, raw_input().split())
    answer = 0
    maxPossibleSpeed = 100000000000000000000
    for i in range(n):
        if maxPossibleSpeed > a[i]:
            maxPossibleSpeed = a[i]
            answer += 1
    print answer
