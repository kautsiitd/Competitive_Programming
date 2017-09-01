import collections

for _ in range(input()):
    s = raw_input()
    countDict = collections.Counter(s)
    ans = ""
    for i in range(65,91):
        if i%10 == i/10:
            if countDict[str(i%10)] > 1:
                ans += chr(i)
        elif countDict[str(i%10)] > 0 and countDict[str(i/10)] > 0:
            ans += chr(i)
    print ans
