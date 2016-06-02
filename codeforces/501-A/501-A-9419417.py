a,b,c,d=map(int,raw_input().split())
l=max(3*a/10,a-((a/250)*c))
k=max(3*b/10,b-((b/250)*d))
if l==k:
    print "Tie"
elif l>k:
    print "Misha"
else:
    print "Vasya"