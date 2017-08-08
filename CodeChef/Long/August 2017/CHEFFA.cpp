#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define mod 1000000007

ll a[131][131];
ll mat[51][131][131];
int arr[50],n;

ll find(int i, int j) {
  if(i>j) return a[j][j];
  else return a[i][j];
}

ll findAns(int level, ll firstNum, ll secondNum) {
  if(level == n-2) {
    return a[firstNum][secondNum];
  }
  else if(mat[level][firstNum][secondNum] != -1) {
    return mat[level][firstNum][secondNum];
  }
  else {
    ll ans = 0;
    rep(k,min(firstNum,secondNum)+1) ans += findAns(level+1,secondNum-k,arr[level+2]+k)%mod;
    ans %= mod;
    mat[level][firstNum][secondNum] = ans;
    return ans;
  }
}

int main() {
  rep(i,131) rep(j,131) a[i][j] = 1;
  rep(i,131) rep(j,131) {
    ll ans = 0;
    rep(k,min(i,j)+1) ans += find(j-k,k)%mod;
    a[i][j] = ans%mod;
  }

  int t;
  cin>>t;
  rep(_,t) {
    rep(level,51) rep(i,131) rep(j,131) mat[level][i][j] = -1;
    cin>>n;
    rep(i,n) cin>>arr[i];
    if(n == 1) {
      cout<<1<<'\n';
    }
    else {
      cout<<findAns(0,arr[0],arr[1])<<'\n';
    }
  }
  return 0;
}
