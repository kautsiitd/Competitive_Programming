n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
answer = 0
def getProduct(index, product):
    global answer
    if index == n:
        if product <= k:
            answer += 1
        return
    getProduct(index + 1, product)
    getProduct(index + 1, product * a[index])
getProduct(0, 1)
print answer - 1
