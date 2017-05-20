from operator import mul
n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
a.sort()
answer1 = 0

def getProduct1(index, product):
    global answer1
    if index == n:
        if product <= k:
            answer1 += 1
        return
    getProduct1(index + 1, product)
    product = product * a[index]
    if product <= k:
        getProduct1(index + 1, product)
    else :
        return
def method1():
    global answer1
    if reduce(mul, a, 1) <= k:
        return pow(2, n) - 1
    else :
        getProduct1(0, 1)
        print answer1 - 1

p = [1]
for i in range(1, n+1):
    p.append(p[i-1] * 2)
answer2 = pow(2, n) - 1
def getProduct2(index, product):
    global answer2
    if index == -1:
        if product > k:
            answer2 -= 1
        return
    getProduct2(index - 1, product)
    product = product * a[index]
    if product <= k:
        getProduct2(index - 1, product)
    else :
        answer2 -= p[index]
        return
def method2():
    global answer2
    getProduct2(n-1, 1)
    print answer2

tempProduct = 1
l = len(a)
mark = l
for i in range(l):
    e = a[i]
    tempProduct *= e
    if tempProduct > k:
        mark = i
        break
if mark <= n/2:
    method1()
else:
    method2()
