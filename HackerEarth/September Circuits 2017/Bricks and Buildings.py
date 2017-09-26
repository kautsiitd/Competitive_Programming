frq = [0 for i in range(100005)]
for _ in range(input()):
    frq[input()] += 1
ans = [0 for i in range(100005)]
for i in range(1,100005):
    j = 1
    while i*j < 100005:
        ans[i] += frq[i*j]
        j += 1
for _ in range(input()):
    print ans[input()]
