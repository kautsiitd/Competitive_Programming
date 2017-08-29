import math

mod = 1000000007

divisors = [[]]+[[j for j in range(i,100001,i)] for i in range(1,100001)]

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
            affectedPos = divisors[index]
            for pos in affectedPos:
                if pos > n:
                    break
                ans[pos] -= oldNum*oldNum
                ans[pos] += newNum*newNum
                ans[pos] %= mod
