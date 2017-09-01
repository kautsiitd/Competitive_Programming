#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i,s,e) for(int i=s;i<e;i++)
#define repi(i,s,e) for(int i=s;i>e;i--)
#define mod 1000000007

struct query {
  int type,l,r;
};

struct node {
  node *left,*right;
  int lower,upper;
  ll value;
};

node* createSegmentTree(int lower, int upper, ll initialValue) {
  node* head = new node();
  head->lower = lower;
  head->upper = upper;
  head->value = 0;
  if(lower == upper) {
    head->value = initialValue;
    return head;
  }
  else {
    int mid = (lower+upper)/2;
    head->left = createSegmentTree(lower,mid,initialValue);
    head->right = createSegmentTree(mid+1,upper,initialValue);
    return head;
  }
}

ll getValue(node* head, int index) {
  if(head->lower == head->upper) {
    return (head->value)%mod;
  }
  else {
    int mid = (head->lower+head->upper)/2;
    if(index <= mid) {
      return (head->value+getValue(head->left,index))%mod;
    }
    else {
      return (head->value+getValue(head->right,index))%mod;
    }
  }
}

void updateRange(node* head, int lower, int upper, ll value) {
  if(head->lower>upper || head->upper<lower) {
    return;
  }
  else if(head->lower>=lower && head->upper<=upper) {
    head->value += value;
    head->value %= mod;
  }
  else {
    updateRange(head->left,lower,upper,value);
    updateRange(head->right,lower,upper,value);
  }
}

int main() {
  int t;
  scanf("%d\n", &t);
  rep(_,0,t) {
    int n,m;
    scanf("%d %d\n", &n, &m);
    query queries[m];
    rep(i,0,m) {
      query q;
      scanf("%d %d %d\n", &q.type, &q.l, &q.r);
      queries[i] = q;
    }
    node* queriesSegmentTree = createSegmentTree(0,m,1);
    node* arraySegmentTree = createSegmentTree(0,n,0);
    repi(i,m-1,-1) {
      query q = queries[i];
      ll value = getValue(queriesSegmentTree,i);
      if(q.type == 1) {
        updateRange(arraySegmentTree,q.l-1,q.r-1,value);
      }
      else {
        updateRange(queriesSegmentTree,q.l-1,q.r-1,value);
      }
    }
    rep(i,0,n) {
      printf("%lld ", getValue(arraySegmentTree,i));
    }
    printf("\n");
  }
  return 0;
}
