def printIt(i,ans):
    print "Case #" + str(i+1) + ":",ans

for _ in range(input()):
    e,n = map(int,raw_input().split())
    powerOf = sorted(map(int,raw_input().split()))

    currentPower = e
    currentHonor = 0
    gainHonorFrom = 0
    sellHonorOfIndex = 0
    gainPowerFrom = n-1
    ans = 0

    while gainPowerFrom > gainHonorFrom:
        while gainPowerFrom > gainHonorFrom and currentPower > powerOf[gainHonorFrom]:
            currentHonor += 1
            ans = max(ans,currentHonor)
            currentPower -= powerOf[gainHonorFrom]
            gainHonorFrom += 1

        if sellHonorOfIndex < gainHonorFrom:
            currentPower += powerOf[gainPowerFrom] - powerOf[sellHonorOfIndex]
            gainPowerFrom -= 1
            sellHonorOfIndex += 1
        else:
            break

    printIt(_,ans)
