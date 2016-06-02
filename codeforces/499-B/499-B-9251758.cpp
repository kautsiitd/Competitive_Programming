#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<cmath>
#include<sstream>
#include<algorithm>
using namespace std;
int main(){
	int n,m;
	cin>>n>>m;
	string a[2*m][2];
	for(int i=0;i<m;i++){
		string l1,l2;
		cin>>l1>>l2;
		if(l1.length()<=l2.length()){
			a[2*i][0]=l1;
			a[2*i][1]=l1;
			a[2*i+1][0]=l2;
			a[2*i+1][1]=l1;
		}
		else{
			a[2*i][0]=l1;
			a[2*i][1]=l2;
			a[2*i+1][0]=l2;
			a[2*i+1][1]=l2;
		}
	}
	for(int i=0;i<n;i++){
		string q;
		cin>>q;
		int c=0;
		while(a[c][0]!=q){
			c+=1;
		}
		cout<<a[c][1]<<" ";
	}
	return 0;
}