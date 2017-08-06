#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main() {
  int t;
  cin>>t;
  for(int _=0;_<t;_++) {
    ll numCandidates,numCompanies;
    cin>>numCandidates>>numCompanies;
    ll minSalaries[numCandidates];
    for(int i=0;i<numCandidates;i++) {
      cin>>minSalaries[i];
    }
    ll maxCandidates[numCompanies];
    ll remainOffers[numCompanies];
    vector< pair<ll,ll> > packages(numCompanies);
    for(int i=0;i<numCompanies;i++) {
      ll a,b;
      cin>>a>>b;
      packages[i] = make_pair(a,i);
      maxCandidates[i] = b;
      remainOffers[i] = b;
    }

    sort(packages.begin(),packages.end());
    reverse(packages.begin(),packages.end());

    string hMatrix[numCandidates];
    for(int i=0;i<numCandidates;i++) {
      cin>>hMatrix[i];
    }
    bool companyVisited[numCompanies];
    for(int i=0;i<numCompanies;i++) {
      companyVisited[i] = false;
    }

    ll studentSelected = 0;
    ll total = 0;
    ll companyGotNothing = 0;

    for(int i=0;i<numCandidates;i++) {
      for(int j=0;j<numCompanies;j++) {
        ll k = packages[j].second;
        if(hMatrix[i][k] == '1' && remainOffers[k] > 0 && packages[j].first >= minSalaries[i]) {
          remainOffers[k] -= 1;
          studentSelected += 1;
          total += packages[j].first;
          companyVisited[k] = true;
          break;
        }
      }
    }

    for(int i=0;i<numCompanies;i++) {
      if(!companyVisited[i]) {
        companyGotNothing += 1;
      }
    }

    cout<<studentSelected<<" "<<total<<" "<<companyGotNothing<<'\n';
  }
  return 0;
}
