def printIt(i,ans):
    print "Case #" + str(i+1) + ":",ans

ans = [1000000 for i in range(1001)]
def sol(i,currentSum,currentAns):
    if currentSum > 51:
        return
    elif i == 8:
        ans[currentSum] = min(ans[currentSum],currentAns)
    else:
        sol(i+1,currentSum,currentAns)
        sol(i,currentSum+i*i,currentAns+1)
        sol(i+1,currentSum+i*i,currentAns+1)
sol(1,0,0)

for _ in range(input()):
    printIt(_,ans[input()])
