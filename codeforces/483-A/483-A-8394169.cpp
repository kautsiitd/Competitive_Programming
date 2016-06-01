#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<time.h>
//printf("%d",kanu);
//binary_search(array,array+size,query);
//sort(array,array+size;
using namespace std;

int greatestCommonDivisor(long long m, long long n)
{
    long long r;

    /* Check For Proper Input */
    if((m == 0) || (n == 0))
        return 0;
    else if((m < 0) || (n < 0))
        return -1;

    do
    {
        r = m % n;
        if(r == 0)
            break;
        m = n;
        n = r;
    }
    while(true);

    return n;
}

int main(void)
{
	long long l,r,a,b,c;
    cin>>l>>r;
    if (r-l<=1){
    	printf("-1");
    	return 0;
    }
    int done=0;
    for(int i=0;i<r-l;i++){
    	a=l+i;
    	for(int k=1;k<=r-l-i;k++){
	    	b=a+k;
	    	if(greatestCommonDivisor(a,b)==1){
	    		//cout<<a<<" "<<b<<'\n';
	    		for(int j=1;j<=r-l-k-i;j++){
	    			c=b+j;
	    			if(greatestCommonDivisor(b,c)==1 && greatestCommonDivisor(a,c)!=1){
	    				done=1;
	    				//cout<<b<<" "<<c<<'\n';
	    				cout<<a<<" "<<b<<" "<<c;
	    				break;
	    			}
	    		}
	    	}
    		if(done==1){
    			break;
    		}
    	}
    	if(done==1){
    		break;
    	}
    }
    if(done==0){
    	cout<<-1;
    }
    return 0;
}