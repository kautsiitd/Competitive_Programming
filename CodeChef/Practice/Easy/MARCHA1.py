def findAnswer(answer, i):
    if i == n:
        return False
    if answer + a[i] == m:
        return True
    else:
        if findAnswer(answer + a[i], i+1):
            return True
        else:
            return findAnswer(answer, i+1)

for _ in range(input()):
    n,m = map(int, raw_input().split())
    a = [input() for i in range(n)]
    if findAnswer(0,0):
        print "Yes"
    else:
        print "No"
