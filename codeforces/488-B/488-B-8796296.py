m=input()
a=[]
for i in range(m):
    a.append(input())
def check(t):
    if (t[3]==3*t[0]) and (t[1]+t[2]==4*t[0]):
        return 1
    return 0
if m==0:
    print "YES"
    print 1
    print 1
    print 3
    print 3
elif m==1:
    print "YES"
    x=a[0]
    print 3*x
    print 2*x
    print 2*x
elif m==4:
    a.sort()
    if check(a)==1:
        print "YES"
    else:
        print "NO"
elif m==3:
    a.sort()
    done=0
    if a[2]==3*a[0]:
        print "YES"
        print 4*a[0]-a[1]
        done=1
    if done==0:
        k=[]
        for i in range(3):
            k.append(a[i])
        k.append(3*a[0])
        if check(k)==1:
            print "YES"
            print 3*a[0]
        else:
            k=[]
            if a[2]%3==0:
                k.append(a[2]/3)
                for i in range(3):
                    k.append(a[i])
                if check(k)==1:
                    print "YES"
                    print a[2]/3
                else:
                    print "NO"
            else:
                print "NO"
else:
    a.sort()
    done=0
    if a[1]%3==0:
        k=[]
        k.append(a[1]/3)
        k.append((k[0]*4)-a[0])
        k.append(a[0])
        k.append(a[1])
        k.sort()
        if check(k)==1:
            done=1
            print "YES"
            print k[0]
            print (k[0]*4)-a[0]
    if done==0:
        k=[]
        k.append(a[0])
        k.append(a[1])
        k.append((k[0]*4)-a[1])
        k.append(a[0]*3)
        k.sort()
        if check(k)==1:
            done=1
            print "YES"
            print (k[0]*4)-a[1]
            print a[0]*3
    if done==0:
        if a[1]==a[0]*3:
            print "YES"
            print a[0]*2
            print a[0]*2
            done=1
    if done==0:
        k=[]
        if (a[0]+a[1])%4==0:
            k.append((a[0]+a[1])/4)
            k.append(a[0])
            k.append(a[1])
            k.append(k[0]*3)
            k.sort()
            if check(k)==1:
                print "kanu","YES"
                print (a[0]+a[1])/4
                print 3*((a[0]+a[1])/4)
                done=1
    if done==0:
        print "NO"