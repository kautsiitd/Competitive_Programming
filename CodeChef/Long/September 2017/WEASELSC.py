class ansStruct:
    def __init__(self,ans,leftMin,leftMinLen,rightMin,rightMinLen):
        self.ans = ans
        self.leftMin = leftMin
        self.leftMinLen = leftMinLen
        self.rightMin = rightMin
        self.rightMinLen = rightMinLen

def solve(l,r):
    global temp
    if l == r:
        return ansStruct(temp[l]*(r-l+1),temp[l],1,temp[l],1)
    else:
        mid = (l+r)/2
        ansl = solve(l,mid)
        lenl = mid-l+1
        ansr = solve(mid+1,r)
        lenr = r-mid
        ans = ansStruct(-1,-1,-1,-1,-1)
        ans.leftMin = ansl.leftMin
        ans.rightMin = ansr.rightMin
        if lenl == ansl.leftMinLen and ansl.leftMin == ansr.leftMin:
            ans.leftMinLen = ansl.leftMinLen + ansr.leftMinLen
        else:
            ans.leftMinLen = ansl.leftMinLen
        if lenr == ansr.rightMinLen and ansl.rightMin == ansr.rightMin:
            ans.rightMinLen = ansl.rightMinLen + ansr.rightMinLen
        else:
            ans.rightMinLen = ansr.rightMinLen
        newPossibleAns = 0
        if ansl.rightMin == ansr.leftMin:
            newPossibleAns = ansl.rightMin*(ansl.rightMinLen+ansr.leftMinLen)
        ans.ans = max(ansl.ans,ansr.ans,newPossibleAns)
        return ans

for _ in range(input()):
    n,k = map(int,raw_input().split())
    a = map(int,raw_input().split())
    temp = []
    i = 0
    ans = 0
    while i<n:
        while i<n and a[i]==0:
            i += 1
        while i<n and a[i]!=0:
            temp.append(a[i])
            i += 1
        if temp != []:
            ans = max(ans, solve(0,len(temp)-1).ans)
            temp = []
    print ans
