for _ in range(input()):
    input()
    a = map(int,raw_input().split())
    input()
    b = map(int,raw_input().split())
    answer = "Yes"
    for i in b:
        if i not in a:
            answer = "No"
            break
    print answer
