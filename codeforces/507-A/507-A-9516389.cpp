#include <bits/stdc++.h>
using namespace std;

/*template<size_t dimcount, typename T>
struct multidimensional_vector
{
    typedef std::vector< typename multidimensional_vector<dimcount-1, T>::type > type;
};

template<typename T>
struct multidimensional_vector<0,T>
{
    typedef T type;
};*/

int main(){
	int n,k;
	cin>>n>>k;
	vector< pair<int,int> > a;
	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		a.push_back(make_pair(x,i+1));
	}
	sort(a.begin(),a.end());
	int ans=0;
	while(ans<n && a[ans].first<=k){
		k-=a[ans].first;
		ans+=1;
	}
	cout<<ans<<'\n';
	for(int i=0;i<ans;i++){
		cout<<a[i].second<<" ";
	}
	return 0;
}