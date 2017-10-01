import bisect

n = input()
a = map(int,raw_input().split())
cumSum = [0]
for i in a:
    cumSum.append(cumSum[-1]+i)

s = sum(a)
if s%3 == 0:
    s = s/3
    sIndexes = [i for i in range(1,n) if cumSum[i] == s]
    s2Indexes = [i for i in range(1,n) if cumSum[i] == 2*s]
    ans = 0
    for i in s2Indexes:
        ans += bisect.bisect_left(sIndexes,i)
    print ans
else:
    print 0
