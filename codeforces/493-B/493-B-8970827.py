t=input()
ca=0
cb=0
la=0
lb=0
sa=[]
sb=[]
last=0
for i in range(t):
    x=input()
    if x>0:
        last="first"
        ca+=x
        la+=1
        sa.append(x)
    else:
        last="second"
        cb+=abs(x)
        lb+=1
        sb.append(abs(x))
if ca!=cb:
    if ca>cb:
        print "first"
    else:
        print "second"
else:
    done=0
    for i in range(min(la,lb)):
        if sa[i]>sb[i]:
            print "first"
            done=1
            break
        elif sa[i]<sb[i]:
            print "second"
            done=1
            break
    if done==0:
        if la>lb:
            print "first"
        elif la<lb:
            print "second"
        else:
            print last