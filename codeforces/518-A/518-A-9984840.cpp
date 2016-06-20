#include<bits/stdc++.h>
#define ll long long
#define inf 1e9
#define MOD 1e9+7
#define mp make_pair
using namespace std;

int main(){
	string s,t;
	cin>>s>>t;
	string ans="";
	int l=s.length();
	for(int i=l-1;i>-1;i--){
		if(s[i]=='z'){
			ans='a'+ans;
		}
		else{
			ans=(char)((int)s[i]+1)+ans;
			string temp="";
			for(int j=0;j<i;j++){
				temp+=s[j];
			}
			ans=temp+ans;
			break;
		}
	}
	if(ans==t){
		cout<<"No such string";
	}
	else{
		cout<<ans;
	}
	return 0;
}