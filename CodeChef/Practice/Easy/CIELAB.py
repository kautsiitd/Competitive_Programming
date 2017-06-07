a,b = map(int, raw_input().split())
c = a - b
c = str(c)
if c[0] == '1':
    print "2" + c[1:]
else:
    print "1" + c[1:]
