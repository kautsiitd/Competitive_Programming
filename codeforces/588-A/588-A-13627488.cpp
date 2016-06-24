#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define inf 1000000000000000000
#define MOD 1000000007

int main(){
	std::ios::sync_with_stdio(false);
	ll n;
	cin>>n;
	ll a[n], p[n], temp = inf, ans=0;
	for(int i=0;i<n;i++){
		cin>>a[i]>>p[i];
		temp = min(temp, p[i]);
		ans+= temp*a[i];
	}
	cout<<ans<<'\n';
	return 0;
}