#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<cmath>
#include<sstream>
using namespace std;
int l;
string ad(string num){
	for(int i=0;i<l;i++){
		if(num[i]=='9'){
			num[i]='0';
		}
		else{
			int temp=num[i];
			char ne=temp+1;
			num[i]=ne;
		}
	}
	return num;
}
int main(){
	string n;
	cin>>l>>n;
	string ans=n;
	string current=n;
	for(int i=0;i<10;i++){
		current=ad(current);
		if (current<ans){
			ans=current;
		}
		for(int head=0;head<=l;head++){
			string temp3="";
			temp3+=current[l-1];
			current.insert(0,temp3);
			current.erase(current.begin()+l);
			if (current<ans){
				ans=current;
			}
		}
	}
	cout<<ans;
	return 0;
}