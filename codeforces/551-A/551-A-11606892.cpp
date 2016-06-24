#include <bits/stdc++.h>
#define ll long long
#define MOD 1e9+7
#define inf 1e9
using namespace std;

int main(){
	int n;
	scanf("%d",&n);
	int a[n],b[n];
	for(int i=0;i<n;i++){
		scanf("%d",&a[i]);
		b[i] = a[i];
	}
	sort(a,a+n);
	int mapping[2001];
	for(int i=0;i<n;i++){
		mapping[a[i]]=n-i;
	}
	for(int i=0;i<n-1;i++){
		printf("%d ",mapping[b[i]]);
	}
	printf("%d",mapping[b[n-1]]);
	return 0;
}