import sys
sys.setrecursionlimit(1000000)

lastMatLimit = 131
a = [[1 for i in range(lastMatLimit)] for j in range(lastMatLimit)]
mod = 1000000007

def find(i,j):
    if i>j:
        return a[j][j]
    else:
        return a[i][j]

for i in range(lastMatLimit):
    for j in range(1,lastMatLimit):
        ans = 0
        for k in range(min(i,j)+1):
            ans += find(j-k,k)%mod
        a[i][j] = ans%mod

def findAns(level,firstNum,secondNum):
    if level == n-2:
        return a[firstNum][secondNum]
    elif mat[level][firstNum][secondNum] != -1:
        return mat[level][firstNum][secondNum]
    else:
        ans = 0
        for k in range(min(firstNum,secondNum)+1):
            ans += findAns(level+1,secondNum-k,arr[level+2]+k)%mod
        ans %= mod
        mat[level][firstNum][secondNum] = ans
        return ans

for _ in range(input()):
    mat = [[[-1 for j in range(lastMatLimit)] for i in range(lastMatLimit)] for level in range(51)]
    n = input()
    arr = map(int,raw_input().split())
    if n == 1:
        print 1
        continue
    print findAns(0,arr[0],arr[1])
