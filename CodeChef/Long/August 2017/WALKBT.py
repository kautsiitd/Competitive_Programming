import Queue
import bisect

def LCALength(a,b):
    global n
    answer = n+1
    while a!=b:
        a/=2
        b/=2
        answer-=1
    return n+1-answer

pow2 = []
temp = 1
for _ in range(2001):
    pow2.append(temp)
    temp *= 2

for _ in range(input()):
    n,nq = map(int,raw_input().split())
    mod = pow2[n]
    answer = 1
    visitedNumbers = []
    l = 0
    x = 0
    for __ in range(nq):
        q = raw_input().split()
        if q[0] == "!":
            c = int(q[1])
            x += pow2[c]
            x %= mod
            if not(visitedNumbers):
                answer += n
                visitedNumbers.append(x)
                l += 1
            elif x in visitedNumbers:
                continue
            else:
                index = bisect.bisect(visitedNumbers, x)
                answer += min(LCALength(x,visitedNumbers[index%l]), LCALength(x,visitedNumbers[(index-1)%l]))
                visitedNumbers.append(x)
                l += 1
                visitedNumbers.sort()
        else:
            print answer
