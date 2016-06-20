#include<bits/stdc++.h>
using namespace std;

int main(){
	int n,m;
	cin>>n>>m;
	int k=1;
	while(k!=n+1){
		if(k%4==2){
			for(int i=0;i<m-1;i++){
				cout<<".";
			}
			cout<<"#"<<endl;
		}
		else if(k%4==0){
			cout<<"#";
			for(int i=0;i<m-1;i++){
				cout<<".";
			}
			cout<<endl;
		}
		else{
			for(int i=0;i<m;i++){
				cout<<"#";
			}
			cout<<endl;
		}
		k+=1;
	}
	return 0;
}