#include<iostream>
using namespace std;

long long nCr(int n, int r) {
  long long answer = 1;
  for (int i = 0; i < r; i++) {
    answer*=(n-i);
  }
  for (int i = 1; i <= r; i++) {
    answer/=i;
  }
  return answer;
}

int main() {
  int t;
  cin>>t;
  for (int i = 0; i < t; i++) {
    int n,k;
    cin>>n>>k;
    cout<<nCr(n-1,k-1)<<'\n';
  }
}
