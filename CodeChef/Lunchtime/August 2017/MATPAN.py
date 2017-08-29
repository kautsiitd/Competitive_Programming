for _ in range(input()):
    cost = map(int,raw_input().split())
    s = raw_input()
    for i in s:
        cost[ord(i)-ord('a')] = 0
    print sum(cost)
