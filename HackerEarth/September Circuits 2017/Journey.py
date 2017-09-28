n,m = map(int,raw_input().split())
l = map(int,raw_input().split())
batteryCostFromStartTo = [0]
for i in l:
    batteryCostFromStartTo.append(batteryCostFromStartTo[-1]+i)
c = map(int,raw_input().split())
p = map(int,raw_input().split())
Q = map(int,raw_input().split())

for qc in Q:
    minPriceAtPos = [0]
    for i in range(1,n):
        temp = []
        if qc >= batteryCostFromStartTo[i] - batteryCostFromStartTo[0]:
            minPriceAtPos.append(0)
            continue
        for j in range(i):
            if minPriceAtPos[j] != -1 and c[j] >= batteryCostFromStartTo[i] - batteryCostFromStartTo[j]:
                temp.append(p[j]+minPriceAtPos[j])
        if temp == []:
            minPriceAtPos.append(-1)
        else:
            minPriceAtPos.append(min(temp))
        print minPriceAtPos
    print minPriceAtPos[n-1]
