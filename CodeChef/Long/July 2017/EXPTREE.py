def findGCD(a,b):
    if a==0:
        return b
    else:
        return findGCD(b%a,a)

def powerOf(digit, pow, mod):
    if pow == 0 :
        return 1
    p = powerOf(digit, pow/2, mod) % mod
    p = (p*p)%mod
    if (pow%2 == 0):
        return p
    else:
        return (digit*p)%mod

mod1 = 1000000007;
mod2 = 1000000009;
for _ in range(input()):
    n = input()
    n -= 1
    p = n*(n+1)
    q = 2*(2*n-1)
    gcd = findGCD(p,q)
    p /= gcd
    q /= gcd
    qInverse1 = powerOf(q, mod1-2, mod1)
    qInverse2 = powerOf(q, mod2-2, mod2)
    answer1 = ((p%mod1)*(qInverse1%mod1))%mod1
    answer2 = ((p%mod2)*(qInverse2%mod2))%mod2
    print answer1,
    print answer2
