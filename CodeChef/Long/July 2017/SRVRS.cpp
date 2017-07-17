#include<iostream>
#include<unordered_map>
#include<vector>
#include<tuple>
#include<algorithm>
#include <queue>
using namespace std;
#define ll long long

ll maxCaveSizeX, maxCaveSizeY;
double distWeight, capacityWeight, timeWeight;
ll currentTime = 0;

class ServerData {
  public:
    ll serverNumber, x, y, numberOfComputers;
    vector<ll> compsPower;
    void setValues(ll identity, ll cordX, ll cordY, ll totalComputers, vector<ll> powers) {
      serverNumber = identity;
      x = cordX;
      y = cordY;
      numberOfComputers = totalComputers;
      compsPower = powers;
    }
};

class ComputerData {
  public:
    ll serverNumber, computerNumber, x, y, capacity, timeToHire;
    void setValues(ll parentServer, ll identity, ll cordX, ll cordY, ll timeItTake) {
      serverNumber = parentServer;
      computerNumber = identity;
      x = cordX;
      y = cordY;
      capacity = timeItTake;
      timeToHire = 0;
    }
};

double findWeightOfComp(ComputerData compData) {
  double coordinateWeightage = (compData.x*(maxCaveSizeX - compData.x) + compData.y*(maxCaveSizeY - compData.y))*distWeight;
  double capacityWeightage = compData.capacity*capacityWeight;
  double timeWeightage = (compData.timeToHire - currentTime)*timeWeight;
  double totalWeight = coordinateWeightage + capacityWeightage + timeWeightage;
  return totalWeight;
}

bool operator<(const ComputerData& comp1, const ComputerData& comp2) {
  // return comp1.timeToHire > comp2.timeToHire;
  // return findWeightOfComp(comp1) < findWeightOfComp(comp2);
  return comp1.capacity > comp2.capacity;
}

bool operator>(const ComputerData& comp1, const ComputerData& comp2) {
  // return comp1.timeToHire < comp2.timeToHire;
  // return findWeightOfComp(comp1) > findWeightOfComp(comp2);
  return comp1.capacity < comp2.capacity;
}

bool operator<=(const ComputerData& comp1, const ComputerData& comp2) {
  // return comp1.timeToHire >= comp2.timeToHire;
  // return findWeightOfComp(comp1) <= findWeightOfComp(comp2);
  return comp1.capacity >= comp2.capacity;
}

bool operator>=(const ComputerData& comp1, const ComputerData& comp2) {
  // return comp1.timeToHire <= comp2.timeToHire;
  // return findWeightOfComp(comp1) >= findWeightOfComp(comp2);
  return comp1.capacity <= comp2.capacity;
}

bool operator==(const ComputerData& comp1, const ComputerData& comp2) {
  // return comp1.timeToHire == comp2.timeToHire;
  // return findWeightOfComp(comp1) == findWeightOfComp(comp2);
  return comp1.capacity == comp2.capacity;
}

int main() {
  // std::ios::sync_with_stdio(false);
  // Initialising Input and Storing required Info in defined Structures
  ll totalServers, totalQueries;
  cin>>totalServers>>totalQueries;

  ll slowestCapacity = 0; // max time taken by computer
  maxCaveSizeX = 0;
  maxCaveSizeY = 0;
  ServerData serversData[totalServers];
  ServerData* serverData;

  for (ll serverIndex = 0; serverIndex < totalServers; serverIndex++) {
    serverData = new ServerData();
    ll x,y,numberOfComputers;
    vector<ll> compsPower;
    cin>>x>>y>>numberOfComputers;
    for (ll compNumber = 0; compNumber < numberOfComputers; compNumber++) {
      ll compPower;
      cin>>compPower;
      compsPower.push_back(compPower);
    }
    serverData->setValues(serverIndex+1,x,y,numberOfComputers,compsPower);

    slowestCapacity = max(slowestCapacity, *min_element(serverData->compsPower.begin(), serverData->compsPower.end()));
    maxCaveSizeX = max(maxCaveSizeX, serverData->x);
    maxCaveSizeY = max(maxCaveSizeY, serverData->y);
    serversData[serverIndex] = *serverData;
  }

  // Deciding various weights
  distWeight = 1;
  capacityWeight = -1;
  timeWeight = -1;
  // // single server
  // if(totalServers == 1) {
  //   distWeight = 0;         //weight of coordinates of computer
  //   capacityWeight = -1;    //weight of speed of computer
  //   timeWeight = -1;        //weight in case of computer is busy
  // }
  // // small Network
  // else if(totalServers <= 100) {
  //   distWeight = 1;
  //   capacityWeight = -2;
  //   timeWeight = -1;
  // }
  // // small numberOfTasks
  // else if(totalQueries <= 1000) {
  //   distWeight = 2;
  //   capacityWeight = -2;
  //   timeWeight = -0.5;
  // }
  // // fast Network
  // else if(slowestCapacity <= 1000) {
  //   distWeight = 2;
  //   capacityWeight = -0.5;
  //   timeWeight = -1;
  // }
  // // small Batcave
  // else if(max(maxCaveSizeX, maxCaveSizeY) <= 3000) {
  //   distWeight = 0.5;
  //   capacityWeight = -2;
  //   timeWeight = -1;
  // }

  // making weighted heap for computers
  priority_queue<ComputerData> weightedHeap;
  for (ll serverIndex = 0; serverIndex < totalServers; serverIndex++) {
    ServerData serverData = serversData[serverIndex];
    for (ll compIndex = 0; compIndex < serverData.numberOfComputers; compIndex++) {
      ll compPower = serverData.compsPower[compIndex];
      ComputerData *compData = new ComputerData();
      compData->setValues(serverData.serverNumber,
                        compIndex + 1,
                        serverData.x,
                        serverData.y,
                        compPower);
      weightedHeap.push(*compData);
    }
  }

  // asking for queries
  for (currentTime = 0; currentTime < totalQueries; currentTime++) {
    printf("?\n");
    fflush(stdout);
    ll taskX, taskY;
    cin>>taskX>>taskY;
    vector<ComputerData> unUsableComps;
    ComputerData bestComp = weightedHeap.top();
    weightedHeap.pop();

    while (bestComp.timeToHire > currentTime) {
      unUsableComps.push_back(bestComp);
      bestComp = weightedHeap.top();
      weightedHeap.pop();
    }
    bestComp.timeToHire = currentTime + bestComp.capacity;
    unUsableComps.push_back(bestComp);

    for (vector<ComputerData>::iterator comp = unUsableComps.begin();
        comp != unUsableComps.end();
        ++comp) {
          weightedHeap.push(*comp);
        }
    unUsableComps.clear();

    printf("! %lld %lld\n", bestComp.serverNumber, bestComp.computerNumber);
    fflush(stdout);
  }
  printf("end\n");
  fflush(stdout);
  return 0;
}
