#include<bits/stdc++.h>
using namespace std;
#define inf 1e4
#define ll long long

int main(){
	ll x,y,s;
	cin>>x>>y>>s;
	x=abs(x);
	y=abs(y);
	if(s<x+y || (s-x-y)%2==1){
		cout<<"No"<<endl;
	}
	else{
		cout<<"Yes"<<endl;
	}
	return 0;
}