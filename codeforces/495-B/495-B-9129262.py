a,b=map(int,raw_input().split())
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
if a<b:
    print 0
elif a==b:
    print "infinity"
else:
    s=list(factors(a-b))
    s.sort()
    count=1
    while count<=len(s) and s[count-1]<=b:
        count+=1
    print len(s)-count+1