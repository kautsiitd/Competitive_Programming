mod = 1000000007
powTwo = [1]
for _ in range(100005):
    powTwo.append((powTwo[-1]*2)%mod)

for _ in range(input()):
    v,e,k = map(int,raw_input().split())
    for __ in range(e):
        a,b = map(int,raw_input().split())
    if v == 1:
        print 0
    else:
        print (powTwo[v-2]*e)%mod
