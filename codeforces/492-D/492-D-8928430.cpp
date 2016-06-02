#include <iostream>
#include <string>
static int a[3000000];
using namespace std;
int main(){
    int n,fx,fy;
    cin>>n>>fx>>fy;
    a[0]=2;
    int j=1,fa=1,fb=1;
    for(int i=1;j<fx+fy-1;i++){
    	if (fa/(fx*1.0)<fb/(fy*1.0)){
        	fa+=1;
        	a[j]=0;
        	j+=1;
        }
    	else if (fa/(fx*1.0)>fb/(fy*1.0)){
        	fb+=1;
        	a[j]=1;
        	j+=1;
        }
    	else{
        	fa+=1;
        	fb+=1;
        	a[j]=2;
        	j+=1;
        	a[j]=2;
        	j+=1;
        }
    }
    a[j]=2;
    for(int i=0;i<n;i++){
    	int q;
    	cin>>q;
    	if(a[q%(fx+fy)]==0){
    		cout<<"Vanya"<<'\n';
    	}
    	else if(a[q%(fx+fy)]==1){
    		cout<<"Vova"<<'\n';
    	}
    	else{
    		cout<<"Both"<<'\n';
    	}
    }
    return 0;
}