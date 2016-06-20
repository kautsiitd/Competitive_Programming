#include<bits/stdc++.h>
using namespace std;
#define inf 1e4
#define ll long long
int hb[100],hg[100];
int nb,ng;

int main(){
	cin>>nb>>ng;
	int ahb;
	cin>>ahb;
	for(int i=0;i<ahb;i++){
		int index;
		cin>>index;
		hb[index]=1;
	}
	int ahg;
	cin>>ahg;
	for(int i=0;i<ahg;i++){
		int index;
		cin>>index;
		hg[index]=1;
	}
	int temp=nb*ng*max(nb,ng);
	for(int i=0;i<nb*ng*max(nb,ng);i++){
		if(hb[i%nb]==1 || hg[i%ng]==1){
			hb[i%nb]=1;
			hg[i%ng]=1;
		}
	}
	for(int i=0;i<nb;i++){
		//cout<<hb[i]<<endl;
		if(hb[i]==0){
			cout<<"No"<<endl;
			return 0;
		}
	}
	for(int i=0;i<ng;i++){
		//cout<<"g "<<hg[i]<<endl;
		if(hg[i]==0){
			cout<<"No"<<endl;
			return 0;
		}
	}
	cout<<"Yes"<<endl;
	return 0;
}