for _ in range(input()):
    a = raw_input()
    b = raw_input()
    dict = {}
    z = False
    ans = "B"
    for i in a:
        if i in dict and not(i in b):
            ans = "A"
            break
        else:
            if not(i in b):
                z = True
            dict[i] = 1

    if ans == "B" and z:
        ans = "A"
        for i in b:
            if not(i in a):
                ans = "B"
                break
    print ans
