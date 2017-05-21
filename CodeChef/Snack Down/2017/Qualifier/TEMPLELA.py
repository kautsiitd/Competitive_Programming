for i in range(input()):
    n = input()
    a = map(int, raw_input().split())
    if n%2 == 0:
        print "no"
        continue
    b = [i+1 for i in range(n/2)]
    c = [element for element in b]
    b.reverse()
    c.append(n/2 + 1)
    c.extend(b)
    if c == a:
        print "yes"
    else:
        print "no"
