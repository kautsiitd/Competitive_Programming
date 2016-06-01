#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<time.h>
//printf("%d",kanu);
using namespace std;

int binary_search(int array[],int query,int length){
	int low,high,middle;
	low=0;
    high=length-1;
    middle=(high-low)/2;
    while (low!=high && high-low!=1){
        if(query==array[middle]){
            return middle+1;
		}
        else if(query>array[middle]){
        	low=middle;
    	}
        else if(query<array[middle]){
            high=middle;
        }
        middle=low+(high-low)/2;
    }
    if (query==array[low]){
        return low;
    }
    else if (query==array[high]){
        return high;
    }
    else{
        return -1;
    }
}

int main(){
	int n,l,x,y;
	scanf("%d%d%d%d",&n,&l,&x,&y);
	int marks[n];
	for(int i=0;i<n;i++){
		int data;
		scanf("%d",&data);
		marks[i]=data;
	}
	//time.time(times);
	int j,d1,d2,k1[2*n],k2[2*n],a,b,f1,f2;
	j=0;d1=0;d2=0;
	while (j!=n){
        a=marks[j]+x;
        b=marks[j]+y;
        k1[n+j]=a;
        k1[j]=marks[j]-x;
        k2[n+j]=b;
        k2[j]=marks[j]-y;
        if (d1==0){
            f1=binary_search(marks,a,n);
        }
        if (d2==0){
            f2=binary_search(marks,b,n);
        }
        if (f1!=-1 && f2!=-1){
            d2=1;
            d1=1;
            break;
        }
        else if (f2!=-1 && f1==-1){
            d2=1;
        }
        else if (f1!=-1 && f2==-1){
            d1=1;
        }
        j+=1;
    }
    sort(k1, k1 + 2*n);
    sort(k2, k2 + 2*n);
    //printf("f",time.time()-times);
    if (d1==1 && d2==1){
        printf("0\n");
    }
    else if (d1==1 && d2==0){
        printf("1\n");
        printf("%d\n",y);
    }
    else if (d1==0 && d2==1){
        printf("1\n");
        printf("%d\n",x);
    }
    else{
        j=0;
        int f;
        while (j!=2*n){
        	//printf("%d %d\n",k1[j],k2[j]);
        	if (k1[j]>=0 && k1[j]<=l){
	            f=binary_search(k2,k1[j],2*n);
	            if (f!=-1){
	                printf("1\n");
	                printf("%d\n",k1[j]);
	                break;
	            }
        	}
            j+=1;
        }
        if (j==2*n){
            printf("2\n");
            printf("%d %d\n",x,y);
        }
    }
	//printf("%f",time.time()-times);
	return 0;
}