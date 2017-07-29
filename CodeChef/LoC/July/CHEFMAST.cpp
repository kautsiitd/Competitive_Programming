#include<iostream>
#include<map>
using namespace std;
#define ll long long

map<string, pair<string,ll> > dict;
string numbers = "0123456789";

pair<string,ll> minMoves(string num) {
  if(dict.find(num) != dict.end()) {
    return dict[num];
  }
  ll first = atoll(num.substr(0,1).c_str());
  ll second = atoll(num.substr(1,1).c_str());
  string remaining = num.substr(2);
  ll ans = 0;

  for (ll i = second; i > first; i--) {
    pair<string, ll> temp = minMoves(numbers[i]+remaining);
    remaining = temp.first;
    ans += temp.second;
  }
  for (ll i = 0; i < min(first,second)+1; i++) {
    pair<string, ll> temp = minMoves(num[0]+remaining);
    remaining = temp.first;
    ans += temp.second;
  }
  dict[num] = make_pair("9"+remaining,ans);
  return dict[num];
}

int main() {
  std::ios::sync_with_stdio(false);
  dict["00"] = make_pair("0",0);
  for (ll a = 1; a < 10; a++) {
    for (ll b = 0; b < 10; b++) {
      if(a>b) {
        dict[numbers.substr(a,1)+numbers.substr(b,1)] = make_pair(numbers.substr(10-a+b,1),1);
      }
      else {
        dict[numbers.substr(a,1)+numbers.substr(b,1)] = make_pair(numbers.substr(10-a,1),2);
      }
    }
  }
  for (ll b = 1; b < 10; b++) {
    dict["0"+numbers.substr(b,1)] = make_pair('0',1);
  }

  ll t;
  cin>>t;
  for (ll currentTest = 0; currentTest < t; currentTest++) {
    string n;
    cin>>n;
    cout<<minMoves("0"+n).second<<'\n';
  }
  return 0;
}
