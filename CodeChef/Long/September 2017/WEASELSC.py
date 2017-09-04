# Used standard solution for subtask 1 from http://www.geeksforgeeks.org/largest-rectangle-under-histogram/

def solve(tempA,n):
    s = []
    max_area = 0
    i = 0
    while i<n:
        if not(s) or tempA[s[-1]]<=tempA[i]:
            s.append(i)
            i+=1
        else:
            tp = s[-1]
            s.pop()
            if not(s):
                area_with_top = tempA[tp]*i
            else:
                area_with_top = tempA[tp]*(i-s[-1]-1)
            if max_area < area_with_top:
                max_area = area_with_top
    while s:
        tp = s[-1]
        s.pop()
        if not(s):
            area_with_top = tempA[tp]*i
        else:
            area_with_top = tempA[tp]*(i-s[-1]-1)
        if max_area < area_with_top:
            max_area = area_with_top
    return max_area

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
            ans = max(ans, solve(temp,len(temp)))
            temp = []
    print ans
