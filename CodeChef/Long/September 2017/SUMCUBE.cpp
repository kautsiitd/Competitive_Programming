#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define rep(i,s,e) for(int i=s; i<e; i++)
#define pb push_back
#define mp make_pair
#define mod 1000000007

ll powTwo[100005];
vector< vector<int> > graph(100005);
int edgeFrom[100005];
map<pair<int,int>,bool> graphDict;
int v,e,k;

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
void resetVaribles() {
  rep(i,0,100005) {
    graph[i] = vector<int>();
    edgeFrom[i] = 0;
  }
  graphDict = map<pair<int,int>,bool>();
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
  for(auto i: edgeFrom) {
    if(i==0) continue;
    else if(i>=2) TwoEdgeUsingThreeNodes += (i*(i-1))/2;
  }
  TwoEdgeUsingThreeNodesAns = (powTwo[v-3]*TwoEdgeUsingThreeNodes)%mod;
  if(e>=4) {
    TwoEdgeUsingFourNodes = (e*(e-1))/2 - TwoEdgeUsingThreeNodes;
    TwoEdgeUsingFourNodesAns = (powTwo[v-4]*TwoEdgeUsingFourNodes)%mod;
  }
}

void setVariables3() {
  rep(a,1,v+1) {
    int edgesFromA = edgeFrom[a];
    // For 4 Nodes
    if(edgesFromA >= 3) {
      ThreeEdgeUsingFourNodes += (edgesFromA*(edgesFromA-1)*(edgesFromA-2))/6;
    }
    // Dependency on connected nodes b and c
    rep(i,0,edgesFromA) {
      int b = graph[a][i];
      rep(j,i+1,edgesFromA) {
        int c = graph[a][j];
        // For 3 Nodes
        if(graphDict.find(mp(b,c)) != graphDict.end()) {
          ThreeEdgeUsingThreeNodes += 1;
          ThreeEdgeUsingFiveNodes += 1;    // Because of connection between b&c
        }
        // For 5 Nodes
        ThreeEdgeUsingFiveNodes += e-edgeFrom[a]-edgeFrom[b]-edgeFrom[c]+2;
      }
    }
  }
  ThreeEdgeUsingThreeNodes /= 3;
  // For 4 Nodes Straight Lines
  ll temp = 0;
  rep(a,1,v+1) {
    int edgesFromA = edgeFrom[a];
    rep(i,0,edgesFromA) {
      int b = graph[a][i];
      rep(j,0,edgeFrom[b]) {
        int c = graph[b][j];
        if(c == a) {
          continue;
        }
        temp += edgeFrom[c]-1;
        if(graphDict.find(mp(a,c)) != graphDict.end()) {
          temp -= 1;
        }
      }
    }
  }
  ThreeEdgeUsingFourNodes += temp/2;
  ThreeEdgeUsingSixNodes = ((e*(e-1)*(e-2))/6) - (ThreeEdgeUsingThreeNodes+ThreeEdgeUsingFourNodes+ThreeEdgeUsingFiveNodes);
  // printf("%lld %lld %lld %lld\n", ThreeEdgeUsingThreeNodes,ThreeEdgeUsingFourNodes,ThreeEdgeUsingFiveNodes,ThreeEdgeUsingSixNodes);
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
  int t;
  scanf("%d\n", &t);
  rep(_,0,t) {
    resetVaribles();
    scanf("%d %d %d\n",&v,&e,&k);
    rep(__,0,e) {
      int a,b;
      scanf("%d %d\n",&a,&b);
      graph[a].pb(b);
      graph[b].pb(a);
      edgeFrom[a] += 1;
      edgeFrom[b] += 1;
      graphDict[mp(a,b)] = true;
      graphDict[mp(b,a)] = true;
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
        // printf("%lld %lld %lld %lld %lld %lld %lld\n",OneEdgeUsingTwoNodesAns,TwoEdgeUsingThreeNodesAns,TwoEdgeUsingFourNodesAns,ThreeEdgeUsingThreeNodesAns,ThreeEdgeUsingFourNodesAns,ThreeEdgeUsingFiveNodesAns,ThreeEdgeUsingSixNodesAns);
        TwoEdgeUsingThreeNodesAns = (6*TwoEdgeUsingThreeNodesAns)%mod;
        TwoEdgeUsingFourNodesAns = (6*TwoEdgeUsingFourNodesAns)%mod;
        ll finalAns = (OneEdgeUsingTwoNodesAns+TwoEdgeUsingThreeNodesAns+TwoEdgeUsingFourNodesAns+ThreeEdgeUsingThreeNodesAns+ThreeEdgeUsingFourNodesAns+ThreeEdgeUsingFiveNodesAns+ThreeEdgeUsingSixNodesAns)%mod;
        printf("%lld\n", finalAns);
      }
    }
  }
  return 0;
}
