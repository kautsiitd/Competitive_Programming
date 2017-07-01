#include<iostream>
using namespace std;

int main() {
  int t;
  cin>>t;
  for (int i = 0; i < t; i++) {
    std::string s;
    cin>>s;
    cout<<min(count(s.begin(),s.end(),'a'), count(s.begin(),s.end(),'b'))<<'\n';
  }
}
