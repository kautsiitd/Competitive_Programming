#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define rep(i,s,e) for(int i=s;i<e;i++)

ull numberOfTwosInFactorial(ull num) {
  ull temp = 2;
  ull ans = 0;
  while(temp <= num) {
    ans += num/temp;
    temp *= 2;
  }
  return ans;
}

int f(ull i, ull j) {
  ull k1 = numberOfTwosInFactorial(i+j);
  ull k2 = numberOfTwosInFactorial(i);
  ull k3 = numberOfTwosInFactorial(j);
  if(k1<=k2+k3) {
    return 1;
  }
  else {
    return 0;
  }
}

int main() {
  rep(i,0,40) {
    rep(j,0,40) {
      cout<<f(i,j)<<" ";
    }
    cout<<'\n';
  }
  return 0;
}
