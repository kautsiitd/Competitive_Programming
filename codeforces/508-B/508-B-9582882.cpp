#include<bits/stdc++.h>
using namespace std;

#define ll long long;
#define ld long double;
string s;
int l;

string func(int i){
	string ans="";
	for(int j=0;j<i;j++){
		ans+=s[j];
	}
	ans+=s[l-1];
	for(int j=i+1;j<l-1;j++){
		ans+=s[j];
	}
	ans+=s[i];
	return ans;
}

int main(){
	int found=0,pfound=0,temp=-1;
	cin>>s;
	l=s.length();
	for(int i=0;i<l;i++){
		//cout<<s[i]%2<<endl;
		if((int)s[i]%2==0){
			if((int)s[l-1]>(int)s[i]){
				s=func(i);
				found=1;
				break;
			}
			else{
				pfound=1;
				temp=i;
			}
		}
	}
	if(found==1){
		cout<<s;
	}
	else if(pfound==1){
		cout<<func(temp);
	}
	else{
		cout<<-1;
	}
	return 0;
}