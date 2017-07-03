pow2 = [1]
[pow2.append(pow2[i]*2) for i in range(64)]

def findChar(atPosition):
    if atPosition <=3:
        return "aac"[atPosition-1]
    elif atPosition in pow2:
        return "a"
    else:
        for i in range(64):
            if pow2[i] > atPosition:
                char = findChar(pow2[i-1]-(atPosition-pow2[i-1]))
                if char == "a":
                    return "c"
                else:
                    return "a"

for _ in range(input()):
    i = input()
    print findChar(i)
