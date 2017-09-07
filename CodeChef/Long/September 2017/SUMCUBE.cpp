#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define rep(i,s,e) for(ll i=s; i<e; i++)
#define pb push_back
#define mp make_pair
#define mod 1000000007

ll powTwo[100005];
vector< vector<ll> > graph(100005);
ll edgeFrom[100005];
ll twoLevelEdgeFrom[100005];
unordered_map<ll,bool> graphDict[100005];
ll v,e,k;

// Variables
// One Edge in expansion
ll OneEdgeUsingTwoNodes = 0;
ll OneEdgeUsingTwoNodesAns = 0;
// Two Edges in expansion
    // using 3 nodes
ll TwoEdgeUsingThreeNodes = 0;
ll TwoEdgeUsingThreeNodesAns = 0;
    // using 4 nodes
ll TwoEdgeUsingFourNodes = 0;
ll TwoEdgeUsingFourNodesAns = 0;
// Three Edges in expansion
    // using 3 nodes
ll ThreeEdgeUsingThreeNodes = 0;
ll ThreeEdgeUsingThreeNodesAns = 0;
    // using 4 nodes
ll ThreeEdgeUsingFourNodes = 0;
ll ThreeEdgeUsingFourNodesAns = 0;
    // using 5 nodes
ll ThreeEdgeUsingFiveNodes = 0;
ll ThreeEdgeUsingFiveNodesAns = 0;
    // using 6 nodes
ll ThreeEdgeUsingSixNodes = 0;
ll ThreeEdgeUsingSixNodesAns = 0;
void resetVaribles(ll v) {
  rep(i,0,v+5) {
    graph[i] = vector<ll>();
    edgeFrom[i] = 0;
    graphDict[i] = unordered_map<ll,bool>();
  }
  OneEdgeUsingTwoNodes = 0;
  TwoEdgeUsingThreeNodes = 0;
  TwoEdgeUsingThreeNodesAns = 0;
  TwoEdgeUsingFourNodes = 0;
  TwoEdgeUsingFourNodesAns = 0;
  ThreeEdgeUsingThreeNodes = 0;
  ThreeEdgeUsingThreeNodesAns = 0;
  ThreeEdgeUsingFourNodes = 0;
  ThreeEdgeUsingFourNodesAns = 0;
  ThreeEdgeUsingFiveNodes = 0;
  ThreeEdgeUsingFiveNodesAns = 0;
  ThreeEdgeUsingSixNodes = 0;
  ThreeEdgeUsingSixNodesAns = 0;
}

void setVariables1() {
  OneEdgeUsingTwoNodes = e;
  OneEdgeUsingTwoNodesAns = (powTwo[v-2]*OneEdgeUsingTwoNodes)%mod;
}

void setVariables2() {
  rep(z,1,v+1) {
    ll i = edgeFrom[z];
    if(i==0) continue;
    else if(i>=2) TwoEdgeUsingThreeNodes += (i*(i-1))/2;
  }
  TwoEdgeUsingThreeNodesAns = (powTwo[v-3]*TwoEdgeUsingThreeNodes)%mod;
  if(v>=4) {
    TwoEdgeUsingFourNodes = (e*(e-1))/2 - TwoEdgeUsingThreeNodes;
    TwoEdgeUsingFourNodesAns = (powTwo[v-4]*TwoEdgeUsingFourNodes)%mod;
  }
}

bool compareForSort(pair<ll,ll> i1, pair<ll,ll> i2) {
    return (i1.second < i2.second);
}

void solveForTriangles() {
  pair<ll,ll> vAndE[v];
  rep(i,1,v+1) {
    vAndE[i-1] = mp(i,edgeFrom[i]);
  }
  sort(vAndE,vAndE+v,compareForSort);
  bool isNodePresent[v+1];
  rep(i,0,v+1) {
    isNodePresent[i] = true;
  }
  for(auto z: vAndE) {
    ll a = z.first;
    ll edgesFromA = edgeFrom[a];
    rep(i,0,edgesFromA) {
      ll b = graph[a][i];
      if(isNodePresent[b]) {
        rep(j,i+1,edgesFromA) {
          ll c = graph[a][j];
          if(isNodePresent[c] && graphDict[b].find(c) != graphDict[b].end()) {
            ThreeEdgeUsingThreeNodes += 1;
          }
        }
      }
    }
    isNodePresent[a] = false;
  }
}

void setVariables3() {
  // For 3 Nodes
  solveForTriangles();
  // For 4 Nodes
  ll temp1=0,temp2 = 0;
  ll count2 = 0;
  rep(a,1,v+1) {
    ll edgesFromA = edgeFrom[a];
    if(edgesFromA >= 3) {
      temp1 += (edgesFromA*(edgesFromA-1)*(edgesFromA-2))/6;
      temp1 %= mod;
    }
    rep(i,0,edgesFromA) {
      ll b = graph[a][i];
      temp2 += twoLevelEdgeFrom[b]-edgesFromA+1;
    }
  }
  temp2 >>= 1;
  temp2 -= 3*ThreeEdgeUsingThreeNodes; // Because of connection between b&c
  ThreeEdgeUsingFourNodes = temp1 + temp2;
  ThreeEdgeUsingFourNodes %= mod;
  // For 5 Nodes
  rep(a,1,v+1) {
    ll twoLevelEdge = twoLevelEdgeFrom[a];
    ThreeEdgeUsingFiveNodes += twoLevelEdge;
  }
  ThreeEdgeUsingFiveNodes /= 2;
  ThreeEdgeUsingFiveNodes *= (e-2);
  ThreeEdgeUsingFiveNodes -= 3*temp1;
  ThreeEdgeUsingFiveNodes -= 2*temp2;
  ThreeEdgeUsingFiveNodes -= 3*ThreeEdgeUsingThreeNodes;
  ThreeEdgeUsingFiveNodes += mod;
  ThreeEdgeUsingFiveNodes %= mod;
  // For 6 Nodes
  // printf("%lld %lld\n", ((e*(e-1)*(e-2))/6)%mod, (ThreeEdgeUsingThreeNodes+ThreeEdgeUsingFourNodes+ThreeEdgeUsingFiveNodes)%mod);
  ThreeEdgeUsingSixNodes = ((((e*(e-1)*(e-2))/6)%mod) - ((ThreeEdgeUsingThreeNodes+ThreeEdgeUsingFourNodes+ThreeEdgeUsingFiveNodes)%mod) + mod)%mod;
  // printf("%lld %lld %lld %lld\n", ThreeEdgeUsingThreeNodes,ThreeEdgeUsingFourNodes,ThreeEdgeUsingFiveNodes,ThreeEdgeUsingSixNodes);
  // Calculating answers
  if(v>=3) ThreeEdgeUsingThreeNodesAns = (6*(powTwo[v-3]*ThreeEdgeUsingThreeNodes)%mod)%mod;
  if(v>=4) ThreeEdgeUsingFourNodesAns = (6*(powTwo[v-4]*ThreeEdgeUsingFourNodes)%mod)%mod;
  if(v>=5) ThreeEdgeUsingFiveNodesAns = (6*(powTwo[v-5]*ThreeEdgeUsingFiveNodes)%mod)%mod;
  if(v>=6) ThreeEdgeUsingSixNodesAns = (6*(powTwo[v-6]*ThreeEdgeUsingSixNodes)%mod)%mod;
}

int main() {
  powTwo[0] = 1;
  rep(i,1,100005) {
    powTwo[i] = (powTwo[i-1]*2)%mod;
  }
  ll t;
  scanf("%lld\n", &t);
  rep(_,0,t) {
    scanf("%lld %lld %lld\n",&v,&e,&k);
    resetVaribles(v);
    rep(__,0,e) {
      ll a,b;
      scanf("%lld %lld\n",&a,&b);
      graph[a].pb(b);
      graph[b].pb(a);
      edgeFrom[a] += 1;
      edgeFrom[b] += 1;
      graphDict[a][b] = true;
      graphDict[b][a] = true;
    }

    rep(a,1,v+1) {
      ll edgesFromA = edgeFrom[a];
      ll temp = 0;
      rep(i,0,edgesFromA) {
        ll b = graph[a][i];
        temp += edgeFrom[b]-1;
      }
      twoLevelEdgeFrom[a] = temp;
    }

    if(v==1 || e==0) {
      printf("%d\n",0);
    }
    else if(v==2) {
      printf("%d\n",1);
    }
    else {
      if(k == 1) {
        setVariables1();
        printf("%lld\n",(OneEdgeUsingTwoNodesAns)%mod);
      }
      else if(k == 2) {
        setVariables1();
        setVariables2();
        TwoEdgeUsingThreeNodesAns = (2*TwoEdgeUsingThreeNodesAns)%mod;
        TwoEdgeUsingFourNodesAns = (2*TwoEdgeUsingFourNodesAns)%mod;
        ll finalAns = (OneEdgeUsingTwoNodesAns+TwoEdgeUsingThreeNodesAns+TwoEdgeUsingFourNodesAns)%mod;
        printf("%lld\n", finalAns);
      }
      else {
        setVariables1();
        setVariables2();
        setVariables3();
        TwoEdgeUsingThreeNodesAns = (6*TwoEdgeUsingThreeNodesAns)%mod;
        TwoEdgeUsingFourNodesAns = (6*TwoEdgeUsingFourNodesAns)%mod;
        // printf("%lld %lld %lld %lld %lld %lld %lld\n",OneEdgeUsingTwoNodesAns,TwoEdgeUsingThreeNodesAns,TwoEdgeUsingFourNodesAns,ThreeEdgeUsingThreeNodesAns,ThreeEdgeUsingFourNodesAns,ThreeEdgeUsingFiveNodesAns,ThreeEdgeUsingSixNodesAns);
        ll finalAns = (OneEdgeUsingTwoNodesAns+TwoEdgeUsingThreeNodesAns+TwoEdgeUsingFourNodesAns+ThreeEdgeUsingThreeNodesAns+ThreeEdgeUsingFourNodesAns+ThreeEdgeUsingFiveNodesAns+ThreeEdgeUsingSixNodesAns)%mod;
        printf("%lld\n", finalAns);
      }
    }
  }
  return 0;
}
