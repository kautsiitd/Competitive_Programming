for _ in range(input()):
    n = input()
    ans = [n]
    for i in range(1,n):
        if i%2 == 0:
            ans.append(n+(i/2))
        else:
            ans.append(n-(i/2)-1)
    ans.sort()
    for i in ans:
        print i,
    print ""
