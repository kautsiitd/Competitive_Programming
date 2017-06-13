// #include "bits/stdc++.h"
#include <iostream>
#include <vector>
using namespace std;
#define ll long long
#define inf 1e10

int main(){
	std::ios::sync_with_stdio(false);
  ll mod = 1000000007;
	int t;
	cin>>t;
	for(int z=0;z<t;z++) {
    int n,k;
    cin>>n>>k;
    int length[n];
    vector<vector<int> > a;
    for(int i=0;i<n;i++){
      cin>>length[i];
      a.push_back(vector<int>());
      for(int j=0;j<length[i];j++){
        int temp;
        cin>>temp;
        a[i].push_back(temp);
      }
      sort(a[i].begin(),a[i].end());
    }

    int answer = 0;
    for(int i=0;i<n;i++) {
      for(int j=i+1;j<n;j++) {
        int indexA = 0;
        int indexB = 0;
        int isPerfect = true;
        for(int unionNumber=1;unionNumber<k+1;unionNumber++) {
          int oldIndexA = indexA;
          int oldindexB = indexB;
          while(indexA<length[i] && a[i][indexA] == unionNumber) {
            indexA +=1;
          }
          while(indexB<length[j] && a[j][indexB] == unionNumber) {
            indexB +=1;
          }
          if(indexA == oldIndexA && indexB == oldindexB) {
            isPerfect= false;
            break;
          }
        }
        if(isPerfect) {
          answer += 1;
        }
      }
    }
    cout<<answer<<'\n';
  }
  return 0;
}
