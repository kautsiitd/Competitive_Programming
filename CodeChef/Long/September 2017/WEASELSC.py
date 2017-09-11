def solveIncreasing(currentIndex,lastValue,ans,kRemain):
    global finalAns
    print currentIndex,lastValue,ans,kRemain
    if currentIndex == n:
        finalAns = max(ans,finalAns)
    else:
        for value in posValues[currentIndex]:
            if value<lastValue:
                finalAns = max(ans,finalAns)
                continue
            elif currentIndex == 0 or value==lastValue:
                solveIncreasing(currentIndex+1,value,ans+value,kRemain)
            else:
                if kRemain > 0:
                    solveIncreasing(currentIndex+1,value,ans+value,kRemain-1)
                else:
                    finalAns = max(ans,finalAns)
                    continue

for _ in range(input()):
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    posValues = []
    for i in range(0,n):
        temp = [0]
        if a[i] == 0:
            continue
        temp.append(a[i])
        if(i>0 and a[i]>a[i-1]):
            temp.append(a[i-1])
        if(i<n-1 and a[i]>a[i+1]):
            if i!=0 and a[i-1] != a[i+1]:
                temp.append(a[i+1])
            else:
                temp.append(a[i+1])
        posValues.append(temp)
    print posValues

    finalAns = 0
    solveIncreasing(0,0,0,k)
    print finalAns
