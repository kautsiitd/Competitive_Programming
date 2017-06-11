#include "bits/stdc++.h"
// #include <iostream>
// #include <vector>
using namespace std;
#define ll long long
#define inf 1e10

int findPos(ll num, vector<ll> &array, int upper){
  int lower = 0;
  while (lower<upper) {
    int mid = (lower+upper)/2;
    if (array[mid] > num) {
      upper = mid;
    }
    else{
      lower = mid + 1;
    }
  }
  return lower;
}

int main(){
	std::ios::sync_with_stdio(false);
  ll mod = 1000000007;
	int t;
	cin>>t;
	for(int i=0;i<t;i++) {
    int n,m,o,temp;
    cin>>n>>m>>o;

    vector<ll> a,b,c;
    for (int j=0;j<n;j++) {
      cin>>temp;
      a.push_back(temp);
    }
    for (int j=0;j<m;j++) {
      cin>>temp;
      b.push_back(temp);
    }
    for (int j=0;j<o;j++) {
      cin>>temp;
      c.push_back(temp);
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    sort(c.begin(), c.end());

    vector<ll> aCum,cCum;
    temp = 0;
    for (int j=0;j<n+1;j++) {
      aCum.push_back(temp);
      temp += a[j];
      temp%=mod;
    }
    temp = 0;
    for (int j=0;j<o+1;j++) {
      cCum.push_back(temp);
      temp += c[j];
      temp%=mod;
    }

    ll answer = 0;
    for (int j=0;j<m;j++) {
      int aIndex = findPos(b[j], a, n);
      int cIndex = findPos(b[j], c, o);
      answer += ((aCum[aIndex] + ((aIndex*b[j])%mod))%mod) * ((cCum[cIndex] + ((cIndex*b[j])%mod))%mod);
      answer%=mod;
    }
    cout<<answer<<'\n';
  }
}
