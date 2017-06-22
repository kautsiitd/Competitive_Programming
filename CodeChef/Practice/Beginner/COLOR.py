for _ in range(input()):
    n = input()
    s = raw_input()
    print n - max(s.count('B'), s.count('R'), s.count('G'))
