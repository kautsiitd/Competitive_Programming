n,k=map(int,raw_input().split())
a=map(int,raw_input().split())
l=min(a)
if(max(a)-min(a)>k):
    print "NO"
else:
    print "YES"
    for i in range(n):
        for j in range(l):
            print 1,
        for j in range(l,a[i]):
            print j-l+1,
        print ""