import bisect

a = [2,7]
size = 33
for i in range(3,size):
    if i%2 == 0:
        a.append(a[-1]+7)
    else:
        a.append(a[-1]+3*a[-2])
b = a[:16]
c = a[16:]

allowedNumbersB = []
allowedNumbersC = []
def f(currentIndex, tillNowSum, type):
    if currentIndex >= size/2:
        if type == 0:
            allowedNumbersB.append(tillNowSum)
        else:
            allowedNumbersC.append(tillNowSum)
    else:
        if type == 0:
            f(currentIndex+1, tillNowSum+b[currentIndex], 0)
            f(currentIndex+1, tillNowSum, 0)
        else:
            f(currentIndex+1, tillNowSum+c[currentIndex], 1)
            f(currentIndex+1, tillNowSum, 1)
f(0,0,0)
f(0,0,1)
allowedNumbersB = list(set(allowedNumbersB))
allowedNumbersB.sort()
allowedNumbersC = list(set(allowedNumbersC))
allowedNumbersC.sort()

for _ in range(input()):
    n = input()
    ans = "NO"
    for i in allowedNumbersC:
        pos = bisect.bisect(allowedNumbersB, n-i)
        if pos != 0 and allowedNumbersB[pos-1] == n-i:
            ans = "YES"
            break
    print ans
