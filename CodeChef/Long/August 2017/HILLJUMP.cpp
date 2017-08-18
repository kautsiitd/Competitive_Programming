#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define mod 1000000007

int ans[100005][20];
int n,q;

struct node {
  ll lower,upper,value;
  node *right, *left;
}*segmentTreeRoot;

node* buildSegmentTree(ll lower, ll upper) {
  node* root = new node();
  root->lower = lower;
  root->upper = upper;
  root->value = 0;
  if(lower!=upper) {
    root->left = buildSegmentTree(lower,(lower+upper)/2);
    root->right = buildSegmentTree(((lower+upper)/2)+1,upper);
  }
  return root;
}

void updateTree(node* root, ll lower, ll upper, ll value) {
  if(lower>root->upper || upper<root->lower) {
    return;
  }
  else if(root->lower<=upper && root->upper>=lower) {
    root->value += value;
  }
  else {
    updateTree(root->left, lower, upper, value+root->value);
    updateTree(root->right, lower, upper, value+root->value);
    root->value = 0;
  }
}

ll getValue(int index) {
  node* root = segmentTreeRoot;
  ll value = 0;
  while(root->upper != root->lower) {
    value += root->value;
    ll mid = (root->lower+root->upper)/2;
    if(index<=mid) {
      root = root->left;
    }
    else {
      root = root->right;
    }
  }
  return value+root->value;
}

ll findAns(ll i, ll k) {
  int index = 0;
  while(k!=0) {
    while((k&1) == 0 && k!=0) {
      k = k>>1;
      index += 1;
    }
    k = k>>1;
    if(ans[i][index] == -1) {
      break;
    }
    i = ans[i][index];
  }
  if(ans[i][index] != -1) {
    return ans[i][index];
  }
  return i;
}

void calculateAnsArray(ll a[], ll size) {
  // creating basic array, updated first column
  stack<ll> s;
  s.push(0);
  int index = 1;
  ll next;
  while(index<size) {
    next = a[index];
    while(!s.empty() && next > a[s.top()]) {
      ans[s.top()][0] = index;
      s.pop();
    }
    s.push(index);
    index += 1;
  }
  while(!s.empty()) {
    ans[s.top()][0] = -1;
    s.pop();
  }
  // Filling up rest of table
  for(int j=1; j<20; j++) {
    for(int i=0; i<size; i++) {
      if(ans[i][j-1] == -1) {
        ans[i][j] = -1;
      }
      else {
        ans[i][j] = ans[ans[i][j-1]][j-1];
      }
    }
  }
}

// This function looks little faulty
void updateAnsArray(ll terminatingPoint) {
  ll lower = max(terminatingPoint - 101,(ll)1);
  ll upper = min(terminatingPoint + 101,(ll)n);
  stack<ll> s;
  s.push(lower);
  int index = lower+1;
  ll next;
  while(index<upper) {
    next = getValue(index);
    while(!s.empty() && next > getValue(s.top())) {
      if(s.top() <= terminatingPoint) {
        ans[s.top()-1][0] = index-1;
      }
      s.pop();
    }
    s.push(index);
    index += 1;
  }
  while(!s.empty()) {
    if(s.top() <= terminatingPoint) {
      ans[s.top()-1][0] = -1;
    }
    s.pop();
  }
  rep(i,n) {
    rep(j,20) printf("%d ",ans[i][j]);
    cout<<'\n';
  }
  cout<<'\n';
}

int main() {
  scanf("%d %d\n", &n, &q);
  ll a[n];
  rep(i,n) scanf("%lld\n", &a[i]);
  segmentTreeRoot = buildSegmentTree(1,n);
  calculateAnsArray(a,n);

  rep(i,q) {
    int type;
    scanf("%d ", &type);
    if(type == 1) {
      ll i,k;
      scanf("%lld %lld\n", &i, &k);
      printf("%lld\n", findAns(i,k));
    }
    else {
      ll left,right,value;
      scanf("%lld %lld %lld\n", &left, &right, &value);
      updateTree(segmentTreeRoot, left, right, value);
      updateAnsArray(right);
      updateAnsArray(left);
    }
  }
  return 0;
}
