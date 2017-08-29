pows = [pow(2,i) for i in range(65)]

def findPos(k,size):
    if size == n:
        return k
    # odd position
    if k%pows[size+1] < pows[size]:
        newk = (k/pows[size+1])*pows[size+1] + (k%pows[size+1])*2
    else:
        temp = k - (k/pows[size])*pows[size]
        newk = (temp%pows[size+1])*2 + 1
        newk += (k/pows[size+1])*pows[size+1]
    return findPos(newk,size+1)

for _ in range(input()):
    n,k = map(int,raw_input().split())
    print findPos(k,1)
