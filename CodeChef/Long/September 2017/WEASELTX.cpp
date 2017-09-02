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

ull numberOfTwosInFactorialStorage[1000005];
ull numberOfTwosInFactorial(ull num) {
  if(num<1000) {
    return numberOfTwosInFactorialStorage[num];
  }
  ull temp = 2;
  ull ans = 0;
  while(temp <= num) {
    ans += num/temp;
    temp *= 2;
  }
  return ans;
}

ull priorCompu(ull num) {
  ull temp = 2;
  ull ans = 0;
  while(temp <= num) {
    ans += num/temp;
    temp *= 2;
  }
  return ans;
}

int main() {
  rep(i,0,1000005) {
    numberOfTwosInFactorialStorage[i] = priorCompu(i);
  }
  return 0;
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
  rep(_,0,q) {
    ull delta;
    scanf("%llu\n", &delta);
    ull ans = values[0];
    if(delta == 0) {
      printf("%llu\n", ans);
      continue;
    }
    rep(i,1,n) {
      ull k1 = numberOfTwosInFactorial(delta-1+depth[i]);
      ull k2 = numberOfTwosInFactorial(depth[i]);
      ull k3 = numberOfTwosInFactorial(delta-1);
      if(k1<=k2+k3) {
        ans ^= values[i];
      }
    }
    printf("%llu\n", ans);
  }
  return 0;
}
