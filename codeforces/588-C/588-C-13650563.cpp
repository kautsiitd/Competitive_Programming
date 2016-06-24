#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define inf 1000000000000000000
#define MOD 1000000007
ll frq[2000005] = {0};

int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin>>n;
	vector<ll> a(n);
	for(int i=0;i<n;i++){
		cin>>a[i];
		frq[a[i]]+=1;
	}
	ll temp=-1,count=0;
	for(int i=0;i<2000005;i++){
		frq[i+1]+=frq[i]/2;
		frq[i]%=2;
	}
	for(int i=0;i<2000005;i++){
		// cout<<frq[i]<<" ";
		count+=frq[i];
	}
	// cout<<'\n';
	cout<<count<<'\n';
	return 0;
}