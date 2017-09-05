#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define rep(i,s,e) for(int i=s;i<e;i++)

int n,q,maxDepth;
int depth[200005];
vector< vector<int> > graph;
ull xorCumulative[262150];
int preCalLimit = 66;
ull preCalculatedDeltaXor[67][262150];

void dfs(int current, int parent, int currentDepth) {
  for(auto child: graph[current]) {
    if(child != parent) {
      depth[child] = currentDepth + 1;
      dfs(child,current,currentDepth+1);
    }
  }
}

ull solve(ull delta, int start, int end, int range) {
  if(delta < preCalLimit) {
    return preCalculatedDeltaXor[delta+1][end-1]^preCalculatedDeltaXor[delta+1][start-1];
  }
  else if(delta<<1 == end-start+1) {
    int mid = (start+end)>>1;
    return xorCumulative[mid]^xorCumulative[start-1];
  }
  else if(delta<<1 > end-start+1) {
    range = range>>1;
    int newEnd;
    if(end-start+1 > range) {
      newEnd = (start+end)>>1;
    }
    else {
      newEnd = end;
    }
    return solve(delta&(range-1),start,newEnd,range);
  }
  else {
    int mid = (start+end)>>1;
    if(mid>maxDepth) {
      return solve(delta,start,mid,range);
    }
    else {
      return solve(delta,start,mid,range)^solve(delta,mid+1,end,range);
    }
  }
  return 0;
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
  maxDepth = *max_element(depth,depth+n);
  ull upperDeltaLimit = 1;
  while(upperDeltaLimit <= maxDepth) {
    upperDeltaLimit = upperDeltaLimit<<1;
  }

  ull xorAtDepth[maxDepth+1];
  rep(i,0,maxDepth+1) {
    xorAtDepth[i] = 0;
  }
  xorAtDepth[0] = values[0];
  rep(i,1,n) {
    xorAtDepth[depth[i]] ^= values[i];
  }

  xorCumulative[0] = 0;
  rep(i,1,maxDepth+2) {
    xorCumulative[i] = xorAtDepth[i-1]^xorCumulative[i-1];
  }
  ull constant = xorCumulative[maxDepth+1];
  rep(i,maxDepth+2,upperDeltaLimit) {
    xorCumulative[i] = constant;
  }

  ull deltaSol[262150];
  rep(i,0,262150) {
    deltaSol[i] = -1;
  }

  rep(iDelta,1,preCalLimit+1) {
    ull ans = 0;
    preCalculatedDeltaXor[iDelta][0] = 0;
    rep(i,1,maxDepth+2) {
      if(f(iDelta-1,i-1) == 1) {
        ans ^= xorAtDepth[i-1];
        preCalculatedDeltaXor[iDelta][i] = ans;
      }
      else {
        preCalculatedDeltaXor[iDelta][i] = preCalculatedDeltaXor[iDelta][i-1];
      }
    }
    constant = preCalculatedDeltaXor[iDelta][maxDepth+1];
    rep(i,maxDepth+2,upperDeltaLimit) {
      preCalculatedDeltaXor[iDelta][i] = constant;
    }
  }

  rep(_,0,q) {
    ull delta;
    scanf("%llu\n", &delta);
    delta = delta&(upperDeltaLimit-1);
    ull ans = values[0];
    if(delta == 0) {
      printf("%llu\n", ans);
    }
    else if(delta == 1) {
      printf("%llu\n", xorCumulative[maxDepth+1]);
    }
    else if(deltaSol[delta] != -1) {
      printf("%llu\n", deltaSol[delta]);
    }
    else {
      ans = solve(delta-1,1,upperDeltaLimit,upperDeltaLimit);
      deltaSol[delta] = ans;
      printf("%llu\n", ans);
    }
  }
  return 0;
}
