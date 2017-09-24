mod = 1000000007
n = input()
a = map(int,raw_input().split())
temp = 1
for i in a:
    temp *= (i+1)
    temp %= mod
totalWays = temp-1
