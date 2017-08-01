#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
#include <sstream>
using namespace std;
#define ll long long

std::string repeat(int n) {
    std::ostringstream os;
    for(int i = 0; i < n; i++)
        os << "repeat";
    return os.str();
}

struct {
  bool operator()(pair<ll,ll> item1, pair<ll,ll> item2) const {
    if(item1.second > item2.second) {
      return true;
    }
    else if(item1.second < item2.second) {
      return false;
    }
    else {
      if(item1.first >= item2.first) {
        return false;
      }
      else {
        return true;
      }
    }
  }
} customLess;



vector<ll> hist(vector<ll> X) {
  vector<ll> h;
  ll limit = *max_element(X.begin(), X.end());
  for(ll i=0; i<limit+1; i++) {
    h.push_back(0);
  }
  for(auto x:X) {
    h[x] += 1;
  }
  return h;
}

int main() {
  std::ios::sync_with_stdio(false);
  int t;
  cin>>t;
  for (int _=0; _<t; _++) {
    ll n,m;
    cin>>n>>m;
    vector< pair<ll,ll> > intervals;
    for (ll i=0; i<n; i++) {
      ll lower,upper;
      cin>>lower>>upper;
      intervals.push_back(make_pair(lower,upper));
    }
    sort(intervals.begin(), intervals.end(), customLess);
    string k;
    cin>>k;

    vector< pair<ll,ll> > bestIntervals;
    bestIntervals.push_back(intervals[0]);
    ll lowerLevel = intervals[0].first;
    ll remaining = m-1;

    ll i = 1;
    while(i<n) {
      pair<ll,ll> currentInterval = intervals[i];
      if(remaining == 0) {
        break;
      }
      if(currentInterval.first >= lowerLevel) {
        i += 1;
        continue;
      }
      else {
        if(currentInterval.second < lowerLevel) {
          bestIntervals.push_back(currentInterval);
          lowerLevel = currentInterval.first;
          remaining -= 1;
          i += 1;
        }
        else {
          pair<ll,ll> bestInterval;
          ll bestRange = 0;
          while(i < n && currentInterval.second >= lowerLevel-1) {
            ll extraRangeCoverUp = lowerLevel - currentInterval.first;
            if(bestRange < extraRangeCoverUp) {
              bestRange = extraRangeCoverUp;
              bestInterval = currentInterval;
            }
            i += 1;
            if(i<n) {
              currentInterval = intervals[i];
            }
          }
          bestIntervals.push_back(make_pair(bestInterval.first,min(bestInterval.second,lowerLevel)));
          lowerLevel = bestInterval.first;
          remaining -= 1;
        }
      }
    }

    reverse(bestIntervals.begin(),bestIntervals.end());
    vector<ll> shift;
    shift.push_back(bestIntervals[0].first);
    for(vector< pair<ll,ll> >::iterator interval = bestIntervals.begin();
        interval != bestIntervals.end();
        ++interval) {
          for(int i=(*interval).first; i<(*interval).second+1; i++) {
            if(i == shift.back()) {
              continue;
            }
            else {
              shift.push_back(i);
            }
          }
        }

    ll numberOfShifts = shift.size();
    reverse(k.begin(),k.end());

    ll kLen = k.length();
    vector<ll> onePos;
    for(int i=0; i<kLen; i++) {
      if(k[i] == '1') {
        onePos.push_back(i);
      }
    }

    vector<ll> sum = conv(histShift,histOnePos);

    ll carry = 0;
    string ans = "";
    for(ll i=0; i<kLen+shift.back(); i++) {
      ans += to_string((carry+sum[i])%2);
      carry = (carry+sum[i])/2;
    }
    while(carry != 0) {
      ans += to_string(carry%2);
      carry /= 2;
    }

    reverse(ans.begin(),ans.end());
    cout<<ans<<'\n';
  }
  return 0;
}
