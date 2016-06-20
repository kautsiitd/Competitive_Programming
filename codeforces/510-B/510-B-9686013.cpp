#include<bits/stdc++.h>
using namespace std;
vector<string> board;
int n,m;
char start;

int bfs(int i,int j,int pi,int pj){
	board[i][j]=char((int)start+32);
	/*for(int z=0;z<n;z++){
		for(int x=0;x<m;x++){
			cout<<board[z][x];
		}
		cout<<endl;
	}
	cout<<endl;*/
	//cout<<board[i][j]<<endl;
	if(i<n-1 && (board[i+1][j]==start || (int)board[i+1][j]-(int)start==32) && (i+1!=pi || j!=pj)){
		//cout<<(int)board[i+1][j]-(int)start<<endl;
		if((int)board[i+1][j]-(int)start==32){
			return 1;
		}
		else if(bfs(i+1,j,i,j)==1){
			return 1;
		}
	}
	if(i>0 && (board[i-1][j]==start || (int)board[i-1][j]-(int)start==32) && (i-1!=pi || j!=pj)){
		if((int)board[i-1][j]-(int)start==32){
			return 1;
		}
		else if(bfs(i-1,j,i,j)==1){
			return 1;
		}
	}
	if(j<m-1 && (board[i][j+1]==start || (int)board[i][j+1]-(int)start==32) && (i!=pi || j+1!=pj)){
		if((int)board[i][j+1]-(int)start==32){
			return 1;
		}
		else if(bfs(i,j+1,i,j)==1){
			return 1;
		}
	}
	if(j>0 && (board[i][j-1]==start || (int)board[i][j-1]-(int)start==32) && (i!=pi || j-1!=pj)){
		if((int)board[i][j-1]-(int)start==32){
			return 1;
		}
		else if(bfs(i,j-1,i,j)==1){
			return 1;
		}
	}
	return 0;
}

int main(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		string row;
		cin>>row;
		board.push_back(row);
	}
	int find=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<m && find==0;j++){
			if((int)board[i][j]-(int)('A')<30){
				start=board[i][j];
				if(bfs(i,j,-1,-1)==1){
					find=1;
					break;
				}
			}
		}
	}
	/*for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<board[i][j];
		}
		cout<<endl;
	}*/
	if(find==1){
		cout<<"Yes";
	}
	else{
		cout<<"No";
	}
	return 0;
}