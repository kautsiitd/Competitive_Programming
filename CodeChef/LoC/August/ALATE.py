import math

mod = 1000000007
def divisors(n):
    divs = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            if n/i == i:
                divs.append(i)
            else:
                divs.extend([i,n/i])
    return divs

for _ in range(input()):
    n,Q = map(int,raw_input().split())
    a = map(int,raw_input().split())
    ans = [-1]
    for i in range(n):
        temp = 0
        for j in range(i,n,i+1):
            temp += a[j]*a[j]
            temp %= mod
        ans.append(temp)

    for _ in range(Q):
        q = map(int,raw_input().split())
        if q[0] == 1:
            print ans[q[1]]
        else:
            index = q[1]
            oldNum = a[index-1]
            newNum = q[2]
            a[index-1] = newNum
            affectedPos = divisors(index)
            for pos in affectedPos:
                ans[pos] -= oldNum*oldNum
                ans[pos] += newNum*newNum
                ans[pos] %= mod
