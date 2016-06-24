#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define inf numeric_limits<ll>::max()

int main(){
	std::ios::sync_with_stdio(false);
	int n,m;
	cin>>n>>m;
	ll a[m][n],ans[n];
	ll max_vote=-1;
	for(int i=0;i<n;i++){
		ans[i]=0;
	}
	for(int i=0;i<m;i++){
		ll temp = -1,ind=-1;
		for(int j=0;j<n;j++){
			cin>>a[i][j];
			if(a[i][j]>temp){
				ind = j;
				temp = a[i][j];
			}
		}
		ans[ind]+=1;
	}
	int f_ans=-1;
	for(int i=0;i<n;i++){
		if(ans[i]>max_vote){
			max_vote = ans[i];
			f_ans = i+1;
		}
	}
	cout<<f_ans<<'\n';
	return 0;
}