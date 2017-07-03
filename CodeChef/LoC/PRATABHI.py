n,q = map(int,raw_input().split())
a = [0 for i in range(n)]

def solveQuery(index, tillNowXOR, k):
    if tillNowXOR == k:
        return True
    elif index == n:
        return False
    else:
        if tillNowXOR ^ a[index] == k:
            return True
        else:
            if solveQuery(index+1, tillNowXOR ^ a[index], k):
                return True
            else:
                return solveQuery(index+1, tillNowXOR, k)


for _ in range(q):
    query = map(int,raw_input().split())
    if query[0] == 1:
        a[query[1]-1] = query[2]
    else:
        if solveQuery(0, 0, query[1]):
            print "YES"
        else:
            print "NO"
