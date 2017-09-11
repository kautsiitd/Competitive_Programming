#include<bits/stdc++.h>
using namespace std;
#define rep(i,s,e) for(int i=s; i<e; i++)
#define ll long long
#define ull unsigned long long

ull arr[300005],down[300005],up[300005],rightMove[300005],leftMove[300005];
int m,n,Q;

struct node {
  node *leftMove,*rightMove;
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
    head->leftMove = createSegmentTree(lower,mid);
    head->rightMove = createSegmentTree(mid+1,upper);
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
      return head->value+getValue(head->leftMove,index);
    }
    else {
      return head->value+getValue(head->rightMove,index);
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
    updateRange(head->leftMove,lower,upper,value);
    updateRange(head->rightMove,lower,upper,value);
  }
}

ull dfs(int current, int parent, int target, ull c) {
  ull cost1,cost2,cost3,cost4;
  int nextNode;
  if(current%n != n-1 && current+1 != parent) {
    nextNode = current + 1;
    if(nextNode == target) {
      arr[nextNode] += c;
      return rightMove[current];
    }
    else {
      cost1 = rightMove[current] + dfs(nextNode, current, target, c);
    }
  }
  if(current%n != 0 && current-1 != parent) {
    nextNode = current - 1;
    if(nextNode == target) {
      arr[nextNode] += c;
      return leftMove[current];
    }
    else {
      cost2 = leftMove[current] + dfs(nextNode, current, target, c);
    }
  }
  if(current/n != m-1 && current+n != parent) {
    nextNode = current + n;
    if(nextNode == target) {
      arr[nextNode] += c;
      return down[current];
    }
    else {
      cost3 = down[current] + dfs(nextNode, current, target, c);
    }
  }
  if(current/n != 0 && current-n != parent) {
    nextNode = current - n;
    if(nextNode == target) {
      arr[nextNode] += c;
      return up[current];
    }
    else {
      cost4 = up[current] + dfs(nextNode, current, target, c);
    }
  }
  ull minCost = min(cost1,min(cost2,min(cost3,cost4)));
  if(minCost == cost1) arr[current+1] += c;
  else if(minCost == cost2) arr[current-1] += c;
  else if(minCost == cost3) arr[current+n] += c;
  else arr[current-n] += c;
  return minCost;
}

int main() {
  cin>>m>>n>>Q;
  rep(i,0,m-1) {
    rep(j,0,n-1) {
      arr[i*n+j] = 0;
    }
  }
  vector< vector<ull> > graph[m*n];
  ull temp;
  rep(i,0,m-1) {
    rep(j,0,n) {
      int a,b;
      scanf("%llu\n", &temp);
      a = i*n + j;
      b = a + n;
      down[a] = temp;
      up[b] = temp;
    }
  }
  rep(i,0,m) {
    rep(j,0,n-1) {
      int a,b;
      scanf("%llu\n", &temp);
      a = i*n + j;
      b = a + 1;
      rightMove[a] = temp;
      leftMove[b] = temp;
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
    rep(_,0,Q) {
      int type;
      cin>>type;
      if(type == 1) {
        int i1,j1,i2,j2;
        ll c;
        cin>>i1>>j1>>i2>>j2>>c;
        // cout<<i1<<" "<<j1<<" "<<i2<<" "<<j2<<" "<<c<<"\n";
        dfs((i1-1)*n+j1-1, -1, (i2-1)*n+j2-1, c);
        arr[(i1-1)*n+j1-1] += c;
      }
      else {
        int i,j;
        cin>>i>>j;
        // cout<<i<<" "<<j<<"\n";
        cout<<arr[(i-1)*n+j-1]<<'\n';
      }
    }
  }

  return 0;
}
