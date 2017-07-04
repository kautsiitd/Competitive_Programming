for _ in range(input()):
    limak,bob = map(int, raw_input().split())
    for i in range(1000):
        numberOfCandy = i + 1
        if(i & 1):
            bob -= numberOfCandy
        else:
            limak -= numberOfCandy

        if(limak < 0 or bob < 0):
            break
    if limak < 0:
        print "Bob"
    else:
        print "Limak"
