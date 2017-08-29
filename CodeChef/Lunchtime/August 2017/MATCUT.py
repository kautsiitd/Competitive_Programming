def findProduct(parent,start,end,product,length):
    global tempProduct,tempLength
    if start == end:
        tempProduct = values[end]*product
        tempLength = length
    else:
        for child in graph[start]:
            if child != parent:
                findProduct(start,child,end,values[start]*product,length+1)

def checkCube(num):
    count = [0 for i in range(limit+1)]
    for i in range(2,limit+1):
        while num>i and num%i == 0:
            count[i] += 1
            num/=i
    count[num] += 1
    isCube = True
    for i in range(2,limit+1):
        if count[i]%3 != 0:
            isCube = False
            break
    return isCube

for _ in range(input()):
    n = input()
    values = [1]+map(int,raw_input().split())
    limit = max(values)
    graph = [[] for i in range(n+1)]
    for i in range(n-1):
        a,b = map(int,raw_input().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = -1
    for i in range(1,n+1):
        for j in range(i,n+1):
            tempProduct = 1
            tempLength = 1
            findProduct(-1,i,j,1,1)
            if checkCube(tempProduct):
                ans = max(ans,tempLength)
    print ans
