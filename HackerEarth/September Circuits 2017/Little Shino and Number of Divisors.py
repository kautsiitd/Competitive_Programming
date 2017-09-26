mod = 1000000007
n = input()
a = map(int,raw_input().split())

leftMulti = [1]
temp = 1
for i in range(n-1):
    temp *= (a[i]+1)
    temp %= mod
    leftMulti.append(temp)
b = a[::-1]
rightMulti = [1]
temp = 1
for i in range(n-1):
    temp *= (b[i]+1)
    temp %= mod
    rightMulti.append(temp)
rightMulti = rightMulti[::-1]

newA = []
for index in range(n):
    i = a[index]
    newA.append((((i*(i+1))/2)*rightMulti[index]*leftMulti[index])%mod)
totalDivisors = 1
for i in newA:
    totalDivisors *= i+1
    totalDivisors %= mod
print totalDivisors
