n,k,p = map(int, raw_input().split())
k = min(n,k)
a = map(int, raw_input().split())
a.extend(a)
b = [sum(a[:k])]
for i in range(0, 2*n-k):
    b.append(b[i] - a[i] + a[i+k])
b = b[::-1]
l = len(b)

import collections
q = collections.deque()
d = n-k+1
for i in range(d):
    while (q) and b[i] >= b[q[-1]]:
        q.pop()
    q.append(i)

c = []
for i in range(d,l):
    c.append(b[q[0]])
    while (q) and q[0] <= i-d:
        q.popleft()
    while (q) and b[i] >= b[q[-1]]:
        q.pop()
    q.append(i)
c.append(b[q[0]])

pointer = 0
queries = raw_input()
for query in queries:
    if query == '?':
        print c[pointer]
    else:
        pointer += 1
        pointer %= n
