#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define rep(i,s,e) for(int i=s;i<e;i++)

int depth[200005];
vector< vector<int> > graph;

void dfs(int current, int parent, int currentDepth) {
  for(auto child: graph[current]) {
    if(child != parent) {
      depth[child] = currentDepth + 1;
      dfs(child,current,currentDepth+1);
    }
  }
}

ull numberOfTwosInFactorial(ull num) {
  ull temp = 2;
  ull ans = 0;
  while(temp <= num) {
    ans += num/temp;
    temp *= 2;
  }
  return ans;
}

ull twoInFact[524298];

int f(ull i, ull j) {
  ull k1 = twoInFact[i+j];
  ull k2 = twoInFact[i];
  ull k3 = twoInFact[j];
  if(k1<=k2+k3) {
    return 1;
  }
  else {
    return 0;
  }
}

int main() {
  rep(i,0,524290) {
    twoInFact[i] = numberOfTwosInFactorial(i);
  }
  int n,q;
  scanf("%d %d\n", &n, &q);
  rep(_,0,n) {
    graph.push_back(vector<int>());
  }
  rep(_,0,n-1) {
    int a,b;
    scanf("%d %d\n", &a, &b);
    graph[a].push_back(b);
    graph[b].push_back(a);
  }
  ull values[n];
  rep(i,0,n-1) {
    scanf("%llu ", &values[i]);
  }
  scanf("%llu\n", &values[n-1]);

  dfs(0,-1,0);
  int maxDepth = *max_element(depth,depth+n);
  ull upperDeltaLimit = 1;
  while(upperDeltaLimit <= maxDepth) {
    upperDeltaLimit *= 2;
  }

  ull xorAtDepth[maxDepth+1];
  rep(i,0,maxDepth+1) {
    xorAtDepth[i] = 0;
  }
  rep(i,1,n) {
    xorAtDepth[depth[i]] ^= values[i];
  }

  rep(_,0,q) {
    ull delta;
    scanf("%llu\n", &delta);
    delta %= upperDeltaLimit;
    ull ans = values[0];
    if(delta == 0) {
      printf("%llu\n", ans);
      continue;
    }
    rep(i,0,maxDepth+1) {
      if(f(delta-1,i) == 1) {
        ans ^= xorAtDepth[i];
      }
    }
    printf("%llu\n", ans);
  }
  return 0;
}
