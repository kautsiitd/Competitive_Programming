n = input()
arr = map(int, raw_input().split())
s = 0
ans = 0
for ai, bi in zip(arr, sorted(arr)):
    s += ai - bi
    if s == 0:
        ans += 1
print ans