#include<iostream>
#define ui unsigned int
#define ll long long
using namespace std;

ll findGCD(ll a, ll b) {
  if (a == 0) {
    return b;
  }
  return findGCD(b%a, a);
}

ll powerOf(ll digit, ll pow, ll mod) {
  if (pow == 0) {
    return 1;
  }
  ll p = powerOf(digit, pow/2, mod) % mod;
  p = (p*p)%mod;
  if (pow%2 == 0) {
    return p;
  }
  else {
    return (digit*p)%mod;
  }
}

int main() {
  int t;
  cin>>t;
  ll mod1 = 1000000007;
  ll mod2 = 1000000009;
  for (int _=0; _<t; _++) {
    ll n;
    cin>>n;
    if (n==1) {
      cout<<"0 0\n";
      continue;
    }
    n -= 1;
    ll p = n*(n+1);
    ll q = 2*(2*n-1);
    ll gcd = findGCD(p,q);
    p /= gcd;
    q /= gcd;
    ll qInverse1 = powerOf(q, mod1-2, mod1);
    ll qInverse2 = powerOf(q, mod2-2, mod2);
    ll answer1 = ((p%mod1)*(qInverse1%mod1))%mod1;
    ll answer2 = ((p%mod2)*(qInverse2%mod2))%mod2;
    cout<<answer1<<" "<<answer2<<'\n';
  }
  return 0;
}
