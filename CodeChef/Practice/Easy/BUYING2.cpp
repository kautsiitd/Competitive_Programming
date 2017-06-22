#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
  int t;
  cin>>t;
  for (int i = 0; i < t; i++) {
    int n,x;
    cin>>n>>x;
    long long a[n];
    for (int j = 0; j < n; j++) {
      cin>>a[j];
    }
    long long lowest = 10000000000,sum = 0;
    for (int j = 0; j < n; j++) {
      sum += a[j];
      lowest = min(lowest, a[j]);
    }

    if ((sum%x != 0) && (sum/x == (sum-lowest)/x)) {
      cout<<-1<<'\n';
    }
    else {
      cout<<sum/x<<'\n';
    }
  }
}
