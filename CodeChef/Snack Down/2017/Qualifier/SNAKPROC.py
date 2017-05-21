for i in range(input()):
    n = input()
    s = raw_input()
    s = s.replace(".", "")
    l = len(s)/2
    a = "HT"*l
    if s == a:
        print "Valid"
    else:
        print "Invalid"
