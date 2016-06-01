a,m=map(int,raw_input().split())
k=a%m
n=0
last=1
done=0
while n!=10000:
    n+=1
    last=pow(2,n)%m
    ans=(last*k)%m
    if ans==0:
        print "Yes"
        done=1
        break
if done==0:
    print "No"