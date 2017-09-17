import collections

for _ in range(input()):
    letters = collections.Counter(raw_input())
    ans = "no"
    for i in letters:
        if letters[i] > 1:
            ans = "yes"
            break
    print ans
