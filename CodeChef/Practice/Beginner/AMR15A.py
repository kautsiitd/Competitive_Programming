n = input()
a = map(int,raw_input().split())
b = sum([1 for i in a if i%2 == 0])
c = sum([1 for i in a if i%2 == 1])
if b>c:
    print "READY FOR BATTLE"
else:
    print "NOT READY"
