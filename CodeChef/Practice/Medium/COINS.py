d = {}
def findBest(i):
    if i<12:
        return i
    elif i in d:
        return d[i]
    else:
        d[i] = findBest(i/2) + findBest(i/3) + findBest(i/4)
        return d[i]

while True:
    try:
        n = input()
        print findBest(n)
    except Exception as e:
        break
