for _ in range(input()):
    n = input()
    a = map(int, raw_input().split())
    due = 0
    for x in a:
        if not x:
            due += 1100
        else:
            if due:
                due += 100
    print due
