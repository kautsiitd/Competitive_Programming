// Used Standard code from here: http://www.geeksforgeeks.org/clusteringpartitioning-an-array-such-that-sum-of-square-differences-is-minimum/

#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long

ull dp[3001][3001];
ull inf = numeric_limits<ull>::max();
ull a[3001],b[3001],c[3001];

ull minCost(int n, int k) {
    for (int i=0; i<=n; i++)
        for (int j=0;j<=k;j++)
            dp[i][j] = inf;

    dp[0][0] = 0;
    for (int i=1;i<=n;i++)
        for (int j=1;j<=k;j++)
            for (int m=i-1;m>=0;m--) {
              ull cost;
              if(m == 0) {
                cost = (c[i-1])*(c[i-1]);
              }
              else {
                cost = (c[i-1]-c[m-1])*(c[i-1]-c[m-1]);
              }
              if(inf - cost >= dp[m][j-1]) {
                dp[i][j] = min(dp[i][j], dp[m][j-1]+cost);
              }
            }
    return dp[n][k];
}

int main() {
  int t;
  cin>>t;
  while(t--) {
    int n,k,start;
    cin>>n>>k>>start;
    k = min(n,k);
    for(int i=0;i<n;i++) {
      cin>>a[i];
    }
    for(int i=1;i<n;i++) {
      b[i-1] = a[i]-a[i-1];
    }
    ull cum = 0;
    c[0] = 0;
    for(int i=0;i<n;i++) {
      cum += b[i];
      c[i+1] = cum;
    }
    cout <<minCost(n, k)<< endl;
  }
  return 0;
}
