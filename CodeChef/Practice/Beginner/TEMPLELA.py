for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    if n%2 == 0:
        print "no"
    else:
        if a == [i+1 for i in range(n/2)] + [n/2 + 1] + [(n/2)-i for i in range(n/2)]:
            print "yes"
        else:
            print "no"
