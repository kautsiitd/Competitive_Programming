#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<cmath>
#include<sstream>
#include<algorithm>
using namespace std;
#define mod 1000000007
int main(){
	int n;
	cin>>n;
	long long lastd=0,lastother=3;
	for(int i=2;i<=n;i++){
		long long temp=lastd;
		lastd=lastother%mod;
		lastother=((temp*3)%mod+(lastother*2)%mod)%mod;
	}
	cout<<lastd;
	return 0;
}