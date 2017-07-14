mod = 1000000007
for _ in range(input()):
    n = input()
    rowInput = map(int,raw_input().split())
    if n == 1:
        print 2
        a = rowInput[0]
        print (-a)%mod,0,1
    elif n == 2:
        print 4
        a = rowInput[0]
        b = rowInput[1]
        d = a - b
        print pow(d,2)%mod,0,(2*d-4*a)%mod,0,1
    elif n == 3:
        print 8
        a = rowInput[0]
        b = rowInput[1]
        c = rowInput[2]
        d = a-b-c
        e = 2*d-4*a
        f = pow(d,2)-4*b*c
        print pow(f,2)%mod,0,(2*e*f - 64*a*b*c)%mod,0,(2*f+pow(e,2))%mod,0,(2*e)%mod,0,1
    else:
        continue
