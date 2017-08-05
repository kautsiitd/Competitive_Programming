n,q = map(int,raw_input().split())
a = map(int,raw_input().split())

for _ in range(q):
    Q = map(int,raw_input().split())
    if Q[0] == 1:
        current,k = Q[1]-1,Q[2]
        lastBig = a[current]
        lastBigIndex = current
        while(current<n and k>0 and current - lastBigIndex <= 100):
            if a[current] > lastBig:
                lastBig = a[current]
                k-=1
                lastBigIndex = current
            current += 1
        print lastBigIndex+1
    else:
        l,r,x = Q[1:]
        for i in range(l-1,r):
            a[i] += x
