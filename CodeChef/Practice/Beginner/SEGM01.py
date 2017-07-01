for _ in range(input()):
    a = raw_input().strip("0")
    if a != "" and a.count("0") == 0:
        print "YES"
    else:
        print "NO"
