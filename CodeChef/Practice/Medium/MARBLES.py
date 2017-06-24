def nCr(n,r):
    if n-r < r:
        r = n-r
    answer = 1
    for i in range(r):
        answer*=(n-i)
    for i in range(1,r+1):
        answer/=i
    return answer

for _ in range(input()):
    n,k = map(int,raw_input().split())
    print nCr(n-1,k-1)
