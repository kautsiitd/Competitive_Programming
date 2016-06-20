#include<bits/stdc++.h>
#define ll long long
#define inf 1e9
#define MOD 1e9+7
#define mp make_pair
using namespace std;

int main(){
	string s,t;
	cin>>s>>t;
	int sfrq_small[26];
	int sfrq_cap[26];
	int tfrq_small[26];
	int tfrq_cap[26];
	int ls=s.length();
	int lt=t.length();
	for(int i=0;i<26;i++){
		sfrq_small[i]=0;
		sfrq_cap[i]=0;
		tfrq_small[i]=0;
		tfrq_cap[i]=0;
	}
	for(int i=0;i<ls;i++){
		if((int)s[i]-(int)('A')>27){
			sfrq_small[(int)s[i]-(int)('a')]+=1;
		}
		else{
			sfrq_cap[(int)s[i]-(int)('A')]+=1;
		}
	}
	for(int i=0;i<lt;i++){
		if((int)t[i]-(int)('A')>27){
			tfrq_small[(int)t[i]-(int)('a')]+=1;
		}
		else{
			tfrq_cap[(int)t[i]-(int)('A')]+=1;
		}
	}
	int ans1=0,ans2=0;
	for(int i=0;i<26;i++){
		int temp1=min(tfrq_small[i],sfrq_small[i]);
		ans1+=temp1;
		tfrq_small[i]-=temp1;
		sfrq_small[i]-=temp1;
		int temp2=min(tfrq_cap[i],sfrq_cap[i]);;
		ans1+=temp2;
		tfrq_cap[i]-=temp2;
		sfrq_cap[i]-=temp2;
	}
	for(int i=0;i<26;i++){
		ans2+=min(tfrq_cap[i],sfrq_small[i]);
		ans2+=min(tfrq_small[i],sfrq_cap[i]);
	}
	cout<<ans1<<" "<<ans2<<endl;
	return 0;
}