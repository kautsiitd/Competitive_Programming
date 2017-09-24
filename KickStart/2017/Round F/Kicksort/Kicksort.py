def printIt(i,ans):
    print "Case #" + str(i+1) + ":",ans

for _ in range(input()):
    n = input()
    a = map(int,raw_input().split())
    if n < 3:
        printIt(_,"YES")
        continue
    startPoint = 1
    endPoint = n
    ans = "YES"
    while (endPoint-startPoint+1) > 1:
        mid = (endPoint-startPoint)/2
        if a[mid] == endPoint:
            endPoint -= 1
        elif a[mid] == startPoint:
            startPoint += 1
        else:
            ans = "NO"
            break
        del a[mid]
    printIt(_,ans)
