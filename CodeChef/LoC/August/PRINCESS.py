for _ in range(input()):
    s = raw_input()
    l = len(s)
    ans = "NO"
    for i in range(l-1):
        if s[i]==s[i+1]:
            ans = "YES"
            break
    for i in range(l-2):
        if s[i:i+3] == s[i:i+3][::-1]:
            ans = "YES"
            break
    print ans
