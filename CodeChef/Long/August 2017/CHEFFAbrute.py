import sys
sys.setrecursionlimit(1000000)

def f(l):
    global n,ans
    newL = l
    for i in range(1,l):
        if a[i]>0 and a[i-1]>0:
            a[i] -= 1
            a[i-1] -= 1
            if i == l-1:
                a.append(1)
                newL += 1
            else:
                a[i+1] += 1
            if not(" ".join(map(str,a)) in dict):
                dict[" ".join(map(str,a))] = True
                ans += 1
                f(newL)
            a[i] += 1
            a[i-1] += 1
            if i == l-1:
                a.pop()
            else:
                a[i+1] -= 1


for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    dict = {}
    ans = 1
    f(n)
    print ans%1000000007
