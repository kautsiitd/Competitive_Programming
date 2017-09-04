#include<bits/stdc++.h>
using namespace std;
#define rep(i,s,e) for(int i=s; i<e; i++)
#define ll long long
#define ull unsigned long long

struct node {
  node *left,*right;
  int lower,upper;
  ll value;
};

node* createSegmentTree(int lower, int upper) {
  node* head = new node();
  head->lower = lower;
  head->upper = upper;
  head->value = 0;
  if(lower == upper) {
    head->value = 0;
    return head;
  }
  else {
    int mid = (lower+upper)/2;
    head->left = createSegmentTree(lower,mid);
    head->right = createSegmentTree(mid+1,upper);
    return head;
  }
}

ll getValue(node* head, int index) {
  if(head->lower == head->upper) {
    return head->value;
  }
  else {
    int mid = (head->lower+head->upper)/2;
    if(index <= mid) {
      return head->value+getValue(head->left,index);
    }
    else {
      return head->value+getValue(head->right,index);
    }
  }
}

void updateRange(node* head, int lower, int upper, ll value) {
  if(head->lower>upper || head->upper<lower) {
    return;
  }
  else if(head->lower>=lower && head->upper<=upper) {
    head->value += value;
  }
  else {
    updateRange(head->left,lower,upper,value);
    updateRange(head->right,lower,upper,value);
  }
}

int main() {
  int m,n,Q;
  cin>>m>>n>>Q;
  ull temp;
  rep(_,0,m-1) {
    rep(__,0,n) {
      cin>>temp;
    }
  }
  rep(_,0,m) {
    rep(__,0,n-1) {
      cin>>temp;
    }
  }

  if(m == 1) {
    node* head = createSegmentTree(0,n);
    rep(_,0,Q) {
      int type;
      cin>>type;
      if(type == 1) {
        int i1,j1,i2,j2;
        ll c;
        cin>>i1>>j1>>i2>>j2>>c;
        updateRange(head,min(j1-1,j2-1),max(j1-1,j2-1),c);
      }
      else {
        int i,j;
        cin>>i>>j;
        cout<<getValue(head,j-1)<<'\n';
      }
    }
  }
  else {

  }

  return 0;
}
