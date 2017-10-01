n,k = map(int,raw_input().split())
ans = 0
remain = 240-k
for i in range(1,n+1):
    if remain >= 5*i:
        remain -= 5*i
        ans += 1
    else:
        break
print ans
