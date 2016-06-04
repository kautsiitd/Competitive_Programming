#include<bits/stdc++.h>
using namespace std;

#define ll long long;
#define ld long double;

int a[1002][1002];
int check(int x,int y){
	if(a[x][y]==1 && a[x+1][y]==1 && a[x][y+1]==1 && a[x+1][y+1]==1){
		return 1;
	}
	else if(a[x][y]==1 && a[x-1][y]==1 && a[x][y-1]==1 && a[x-1][y-1]==1){
		return 1;
	}
	else if(a[x][y]==1 && a[x+1][y]==1 && a[x][y-1]==1 && a[x+1][y-1]==1){
		return 1;
	}
	else if(a[x][y]==1 && a[x-1][y]==1 && a[x][y+1]==1 && a[x-1][y+1]==1){
		return 1;
	}
	else{
		return 0;
	}
}

int main(){
	int n,m,k,done=0;
	cin>>n>>m>>k;
	for(int i=0;i<1000;i++){
		for(int j=0;j<1000;j++){
			a[i][j]=0;
		}
	}
	for(int i=0;i<k;i++){
		int x,y;
		cin>>x>>y;
		a[x][y]=1;
		int temp=check(x,y);
		if(temp==1){
			cout<<i+1;
			done=1;
			break;
		}
	}
	if(done==0){
		cout<<0;
	}
	return 0;
}