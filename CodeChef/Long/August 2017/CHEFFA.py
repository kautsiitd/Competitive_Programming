import sys
sys.setrecursionlimit(1000000)

def f(l):
    global n,ans
    newL = l
    for i in range(1,l):
        if b[i]>0 and b[i-1]>0:
            b[i] -= 1
            b[i-1] -= 1
            if i == l-1:
                b.append(1)
                newL += 1
            else:
                b[i+1] += 1
            if not(" ".join(map(str,b)) in dict):
                dict[" ".join(map(str,b))] = True
                ans += 1
                f(newL)
            b[i] += 1
            b[i-1] += 1
            if i == l-1:
                b.pop()
            else:
                b[i+1] -= 1

for _ in range(input()):
    al = input()
    a = map(int,raw_input().split())
    if al == 1:
        print 1
        continue
    n = 2
    b = [a[-2],a[-1]]
    dict = {}
    ans = 1
    f(n)
    print ans%1000000007
