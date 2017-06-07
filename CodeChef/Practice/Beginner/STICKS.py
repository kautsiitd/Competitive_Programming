for _ in range(input()):
    n = input()
    a = map(int, raw_input().split())
    a.sort(reverse=True)
    count = 0
    answer = 1
    index = 1
    while index < n:
        if a[index] == a[index-1]:
            count += 1
            answer *= a[index]
            index += 1
            if count == 2:
                break
        index += 1
    if count == 2:
        print answer
    else:
        print -1
