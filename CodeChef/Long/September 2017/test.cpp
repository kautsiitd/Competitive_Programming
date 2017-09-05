#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define rep(i,s,e) for(int i=s;i<e;i++)
#define repi(i,s,e) for(int i=s;i>e;i--)

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
  int n = 9;
  int a[2*n][n];
  rep(i,0,n) {
    cout<<i+1<<"\n";
    rep(j,0,n-1) {
      a[i][j] = f(i,j);
      cout<<a[i][j]<<" ";
    }
    ull temp = 0;
    ull mul = 1;
    repi(j,n-2,0) {
      temp += a[i][j]*mul;
      mul *= 2;
    }
    cout<<temp;
    cout<<'\n';
  }
  // rep(j,0,n) {
  //   cout<<a[5][j]<<" ";
  // }
  // cout<<'\n';
  // cout<<'\n';
  //
  // rep(j,0,n) {
  //   cout<<(a[2][j]^a[4][j]^a[8][j])<<" ";
  // }
  // cout<<'\n';
  return 0;
}
