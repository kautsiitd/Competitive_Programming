def compare(item1, item2):
    if item1[1] > item2[1]:
        return -1
    elif item1[1] < item2[1]:
        return 1
    else:
        if item1[0] > item2[0]:
            return 1
        elif item1[0] < item2[0]:
            return -1
        else:
            return 0

def sum(a,b):
    l1 = len(a)
    l2 = len(b)
    a += "0"*(l2-l1)
    ans = ""
    carry = 0
    for i in range(l2):
        ans += str((int(a[i]) + int(b[i]) + carry)%2)
        carry = (int(a[i]) + int(b[i]) + carry)/2
    if carry == 1:
        ans += "1"
    return ans

def takeInput():
    temp = raw_input()
    while(temp == ""):
        temp = raw_input()
    return temp

for _ in range(int(takeInput())):
    n,m = map(int,takeInput().split())
    intervals = []
    for __ in range(n):
        intervals.append(map(int,takeInput().split()))
    intervals = sorted(intervals, cmp=compare)
    k = takeInput()

    bestIntervals = [intervals[0]]
    lowerLevel = intervals[0][0]
    remaining = m-1

    i = 1
    while i<n:
        currentInterval = intervals[i]
        if remaining == 0:
            break
        if currentInterval[0] >= lowerLevel:
            i += 1
            continue
        else:
            if currentInterval[1] < lowerLevel:
                bestIntervals.append(currentInterval)
                lowerLevel = currentInterval[0]
                remaining -= 1
                i+=1
            else:
                bestInterval = None
                bestRange = 0
                while i < n and currentInterval[1] >= lowerLevel-1:
                    extraRangeCoverUp = lowerLevel - currentInterval[0]
                    if bestRange < extraRangeCoverUp:
                        bestRange = extraRangeCoverUp
                        bestInterval = currentInterval
                    i += 1
                    if i<n:
                        currentInterval = intervals[i]
                bestIntervals.append([bestInterval[0],min(bestInterval[1],lowerLevel)])
                lowerLevel = bestInterval[0]
                remaining -= 1

    bestIntervals = bestIntervals[::-1]
    shift = [bestIntervals[0][0]]
    for interval in bestIntervals:
        for i in range(interval[0],interval[1]+1):
            if i == shift[-1]:
                continue
            else:
                shift.append(i)

    numberOfShifts = len(shift)
    k = k[::-1]
    ans = "0"*shift[0] + k
    for i in range(1,numberOfShifts):
        print ans,"0"*shift[i]+k,sum(ans,"0"*shift[i]+k)
        ans = sum(ans,"0"*shift[i]+k)
    print ans[::-1]
