#include<bits/stdc++.h>
#define ll long long
#define inf 1e9
#define mp make_pair
#define MOD 1000000007
using namespace std;

int main(){
	string s;
	cin>>s;
	int n,z=s.length();
	cin>>n;
	if(z%n!=0){
		cout<<"NO";
	}
	else{
		int l=z/n,cannt=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<l && cannt==0;j++){
				if(s[(i*l)+j]!=s[((i+1)*l)-j-1]){
					cannt=1;
					break;
				}
			}
		}
		if(cannt==0){
			cout<<"YES";
		}
		else{
			cout<<"NO";
		}
	}
	return 0;
}