s=raw_input()
found=0
done=0
for i in range(len(s)/2):
    if s[i]!=s[len(s)-i-1]:
        a=s[:len(s)-i]+s[i]+s[len(s)-i:]
        b=s[:i]+s[len(s)-i-1]+s[i:]
        found=1
        break
if found==0 and len(s)%2==0:
    print s[:len(s)/2]+"a"+s[len(s)/2:]
    done=1
elif found==0 and len(s)%2==1:
    print s[:len(s)/2]+s[len(s)/2]+s[len(s)/2:]
    done=1
elif found==1:
    nota=0
    for i in range(len(a)/2):
        if a[i]!=a[len(a)-i-1]:
            nota=1
            break
    if nota==0:
        print a
        done=1
    notb=0
    if done==0:
        for i in range(len(b)/2):
            if b[i]!=b[len(b)-i-1]:
                notb=1
                break
        if notb==0:
            print b
            done=1
    if done==0:
        print "NA"