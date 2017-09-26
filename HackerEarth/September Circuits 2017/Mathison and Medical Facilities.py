import time
import random
startTime = time.time()

def findProfit(ans):
    totalConstructionCost = sum([constructionCost[i-1] for i in ans])
    clientsWillPay = sum([min([clientPay[i][j-1] for j in ans]) for i in range(m)])
    return clientsWillPay-totalConstructionCost

def findRandomAns():
    temp = [random.randint(1,n-k+1)]
    for i in range(1,k):
        temp.append(random.randint(temp[-1]+1,n-k+i+1))
    return temp

n,k,m = map(int,raw_input().split())
clientPay = [map(int,raw_input().split()) for _ in range(m)]
constructionCost = map(int,raw_input().split())

ans = [i for i in range(1,k+1)]
bestProfit = findProfit(ans)
while time.time()-startTime < 9:
    tempAns = findRandomAns()
    tempProfit = findProfit(tempAns)
    if tempProfit > bestProfit:
        bestProfit = tempProfit
        ans = tempAns

for i in ans:
    print i,
print ""
