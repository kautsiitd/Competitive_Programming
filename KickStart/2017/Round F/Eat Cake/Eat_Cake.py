def printIt(i,ans):
    print "Case #" + str(i+1) + ":",ans

squares = [i*i for i in range(1,102)]
ans = [0,1]
for i in range(2,10001):
    j = 0
    tempAns = 1000000
    while squares[j] <= i:
        tempAns = min(tempAns,1+ans[i-squares[j]])
        j += 1
    ans.append(tempAns)

for _ in range(input()):
    printIt(_,ans[input()])
