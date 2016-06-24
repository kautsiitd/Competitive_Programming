#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define inf numeric_limits<ll>::max()

int main(){
	std::ios::sync_with_stdio(false);
	ll n,m;
	cin>>n>>m;
	if(n==1){
		cout<<1<<'\n';
		return 0;
	}
	if(m==1){
		cout<<2<<'\n';
		return 0;
	}
	if(m==n){
		cout<<n-1<<'\n';
		return 0;
	}
	if(n%2==0){
		if(m>n/2){
			cout<<m-1<<'\n';
		}
		else{
			cout<<m+1<<'\n';
		}
	}
	else{
		if(m>=(n+1)/2){
			cout<<m-1<<'\n';
		}
		else{
			cout<<m+1<<'\n';
		}
	}
	return 0;
}