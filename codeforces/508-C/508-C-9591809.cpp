#include<bits/stdc++.h>
using namespace std;

#define ll long long;
#define ld long double;

int main(){
	int n,t,r,b[303],busy[303],candle[303],ans=0;
	cin>>n>>t>>r;
	for(int i=0;i<303;i++){
		candle[i]=0;
	}
	if(t<r){
		cout<<-1;
		return 0;
	}
	vector<int> bhootgone;
	for(int i=0;i<n;i++){
		int come;
		cin>>come;
		bhootgone.push_back(come+1);
	}
	sort(bhootgone.begin(),bhootgone.end());
	for(int i=n-1;i>-1;i--){
		int putl=t,temp=0;
		while(candle[bhootgone[i]]<r){
			for(int j=bhootgone[i]-t+1+temp;j<=bhootgone[i];j++){
				if(j<0){
					continue;
				}
				candle[j]+=1;
			}
			ans+=1;
			temp+=1;
		}
	}
	cout<<ans;
	return 0;
}