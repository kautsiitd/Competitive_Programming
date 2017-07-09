from fractions import gcd
maxi =10**19
def lcm(x,y):
    return (x*y)/gcd(x,y)

def solve(a,n):
    res=maxi
    for i in range(1,n):
        for j in range(0,i):
            k=lcm(a[i],a[j])
            if k<res:
                res=k
    return res



t=input()
for i in range(t):
    n=input()
    a=sorted(map(int,raw_input().split()))
    print solve(a,n)
