for _ in range(input()):
    d,n = map(int, raw_input().split())
    answer = n
    for _ in range(d):
        answer = (answer*(answer+1))/2
    print answer
