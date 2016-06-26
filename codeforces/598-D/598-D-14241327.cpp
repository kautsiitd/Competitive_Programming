#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define inf std::maxlimits<int>::max();
#define MOD 1000000007

// int main(){
// 	ios::sync_with_stdio(false);
// 	int t;
// 	cin>>t;
// 	for(int i=0;i<t;i++){
// 		ll n;
// 		cin>>n;
// 		ll ans = n*(n+1)/2;
// 		ll temp = 1;
// 		while(temp<n){
// 			temp += (temp^temp>>1)<<1;
// 		}
// 		cout<<ans-(temp<<1)<<'\n';
// 	}
// 	return 0;
// }

// int main(){
// 	ios::sync_with_stdio(false);
// 	string s;
// 	cin>>s;
// 	int m;
// 	cin>>m;
// 	for(int i=0;i<m;i++){
// 		int l,r,k;
// 		cin>>l>>r>>k;
// 		int start = r-(k%(r-l+1))+1;
// 		if(k%(r-l+1)==0){
// 			start = l;
// 		}
// 		string news = "";
// 		for(int j=0;start+j<=r;j++){
// 			news+=s[start+j-1];
// 		}
// 		for(int j=l;j<start;j++){
// 			news+=s[j-1];
// 		}
// 		for(int j=l;j<=r;j++){
// 			s[j-1]=news[j-l];
// 		}
// 	}
// 	cout<<s<<'\n';
// 	return 0;
// }

int ans=0;
int n,m,k;
string a[1002];
int b[1000][1000];

int search(int x,int y){
	a[x][y] = 'd';
	if(x-1>=0){
		if(a[x-1][y]=='.'){
			search(x-1,y);
		}
		else if(a[x-1][y]=='*'){
			ans+=1;
		}
	}
	if(x+1<n){
		if(a[x+1][y]=='.'){
			search(x+1,y);
		}
		else if(a[x+1][y]=='*'){
			ans+=1;
		}
	}
	if(y-1>=0){
		if(a[x][y-1]=='.'){
			search(x,y-1);
		}
		else if(a[x][y-1]=='*'){
			ans+=1;
		}
	}
	if(y+1<m){
		if(a[x][y+1]=='.'){
			search(x,y+1);
		}
		else if(a[x][y+1]=='*'){
			ans+=1;
		}
	}
}

void redo(int x,int y){
	a[x][y] = '.';
	b[x][y] = ans;
	if(x-1>=0){
		if(a[x-1][y]=='d'){
			redo(x-1,y);
		}
	}
	if(x+1<n){
		if(a[x+1][y]=='d'){
			redo(x+1,y);
		}
	}
	if(y-1>=0){
		if(a[x][y-1]=='d'){
			redo(x,y-1);
		}
	}
	if(y+1<m){
		if(a[x][y+1]=='d'){
			redo(x,y+1);
		}
	}
}

int main(){
	ios::sync_with_stdio(false);
	for(int i=0;i<1000;i++){
		for(int j=0;j<1000;j++){
			b[i][j] = 0;
		}
	}
	cin>>n>>m>>k;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}	
	for(int j=0;j<k;j++){
		int x,y;
		cin>>x>>y;
		if(b[x-1][y-1]!=0){
			cout<<b[x-1][y-1]<<'\n';
			continue;
		}
		search(x-1,y-1);
		// printb();
		redo(x-1,y-1);
		// printb();
		cout<<ans<<'\n';
		ans=0;
	}
	return 0;
}