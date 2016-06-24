#include<bits/stdc++.h>
#define ll long long
#define inf 1e9
#define mp make_pair
#define MOD 1000000007
using namespace std;
int coun[600];
struct node{
	int data,lower,higher;
	node *left,*right,*parent;
};

node*tree(node*parent,int lower,int higher){
	node*temp;
	temp=new node;
	if(higher==lower){
		temp->data=coun[lower];
	}
	else{
		temp->left=tree(temp,lower,lower+(higher-lower)/2);
		temp->right=tree(temp,lower+((higher-lower)/2)+1,higher);
		temp->data=max(temp->left->data,temp->right->data);
		temp->parent=parent;
	}
	temp->lower=lower;
	temp->higher=higher;
//	cout<<lower<<" "<<higher<<" "<<temp->data<<'\n';
	return temp;
}

int getmax(int ind,int val,node* cur){
	int lower=cur->lower;
	int higher=cur->higher;
	if(lower==higher){
		cur->data=val;
	}
	else{
		if(ind<=lower+(higher-lower)/2){
			cur->data=max(cur->right->data,getmax(ind,val,cur->left));
		}
		else{
			cur->data=max(cur->left->data,getmax(ind,val,cur->right));
		}
	}
//	cout<<lower<<" "<<higher<<" "<<cur->data<<'\n';
	return cur->data;
}

int main(){
	int n,m,q;
	scanf("%d %d %d",&n,&m,&q);
	int a[n][m];
	for(int i=0;i<n;i++){
		coun[i]=0;
		int temp=0;
		for(int j=0;j<m;j++){
			scanf("%d",&a[i][j]);
			if(a[i][j]==1){
				temp+=1;
			}
			else{
				if(temp>coun[i]){
					coun[i]=temp;
				}
				temp=0;
			}
		}
		if(temp>coun[i]){
			coun[i]=temp;
		}
	}
	node *head;
	head=tree(head,0,n-1);
	for(int i=0;i<q;i++){
		int x,y;
		scanf("%d %d",&x,&y);
		if(a[x-1][y-1]==0){
			a[x-1][y-1]=1;
		}
		else{
			a[x-1][y-1]=0;
		}
		int temp=0;
		coun[x-1]=0;
		for(int j=0;j<m;j++){
			if(a[x-1][j]==1){
				temp+=1;
			}
			else{
				if(temp>coun[x-1]){
					coun[x-1]=temp;
				}
				temp=0;
			}
			if(temp>coun[x-1]){
				coun[x-1]=temp;
			}
		}
//		cout<<"lol"<<coun[x-1]<<'\n';
		int maxi=getmax(x-1,coun[x-1],head);
		printf("%d\n",maxi);
	}
	return 0;
}