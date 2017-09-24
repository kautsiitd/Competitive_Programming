#include<bits/stdc++.h>
using namespace std;
#define rep(i,s,e) for(int i=s; i<e; i++)
#define repi(i,s,e) for(int i=s; i>e; i--)
#define ll long long
#define ull unsigned long long

int arr[100005];
arr[100004] = 100005;

struct node {
  node *leftMove,*rightMove;
  int lower,upper,value;
};

node* createSegmentTree(int lower, int upper) {
  node* head = new node();
  head->lower = lower;
  head->upper = upper;
  if(lower == upper) {
    head->value = lower;
    return head;
  }
  else {
    int mid = (lower+upper)/2;
    head->leftMove = createSegmentTree(lower,mid);
    head->rightMove = createSegmentTree(mid+1,upper);
    if(arr[head->leftMove->value] < arr[head->rightMove->value]) {
      head->value = head->leftMove->value;
    }
    else {
      head->value = head->rightMove->value;
    }
    return head;
  }
}

int getIndexOfMin(node* head, int lower, int upper) {
  if(head->lower >= lower && head->upper <= upper) {
    return head->value;
  }
  else if(head->upper < lower || head->lower > upper) {
    return 100004;
  }
  else {
    int leftMinIndex = getIndexOfMin(head->leftMove, lower, upper);
    int rightMinIndex = getIndexOfMin(head->rightMove, lower, upper);
    if(arr[leftMinIndex] <= arr[rightMinIndex]) {
      return leftMinIndex;
    }
    else {
      return rightMinIndex;
    }
  }
}

int main() {
  int t;
  scanf("%d\n", &t);
  rep(_,0,t) {
    int n,k;
    scanf("%d %d\n", &n, &k);
    rep(i,0,n-1) {
      scanf("%d ", &a[i]);
    }
    scanf("%d\n", &a[n-1]);
    node* minTree = createSegmentTree(0,n-1);

    rep(i,0,n) {
      int lastRangeMin = arr[i];
      int lastRangeMinIndex = i;
      rep(j,i,n) {
        if(lastRangeMin >= arr[j]) {
          lastRangeMin = arr[j];
          lastRangeMinIndex = j;
        }
        int currentMinIndex = lastRangeMinIndex;
        int currentMin = lastRangeMin;
        int currentK = k;
        bool canUseK = true;

        while(currentK != 0 && canUseK) {
          ll areaIncreament = 0;
          int newMinIndex = -1;
          rep(m,currentMinIndex+1,j) {
            int tempMinIndex = getIndexOfMin(m,j);
            ll tempAreaIncreament = ((j-tempMinIndex+1)*arr[tempMinIndex]) + ((tempMinIndex-currentMinIndex)*currentMin);
            if(tempAreaIncreament > areaIncreament) {
              areaIncreament = tempAreaIncreament;
              newMinIndex = tempMinIndex;
            }
          }
          currentK -= 1;
          currentMin = arr[newMinIndex];
          currentMinIndex = newMinIndex;
        }
      }
    }
  }
  return 0;
}
