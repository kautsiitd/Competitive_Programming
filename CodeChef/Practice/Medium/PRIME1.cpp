#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
using namespace std;

vector<int> primeNumbers;

bool checkPrime(long long n) {
  int upperLimit = int(sqrt(n));
  int i = 0;
  while(primeNumbers[i] <= upperLimit) {
    if(n%primeNumbers[i] == 0) {
      return false;
    }
    i += 1;
  }
  return true;
}

void makePrimes() {
  primeNumbers.push_back(2);
  for (int i = 3; i < 32000; i++) {
    if(checkPrime(i)) {
      primeNumbers.push_back(i);
    }
    i += 1;
  }
}

int main() {
  makePrimes();
  int numberOfTest;
  cin>>numberOfTest;
  for (int i = 0; i < numberOfTest; i++) {
    long long n,m;
    cin>>n>>m;
    for (long long j = n; j < m+1; j++) {
      if(j%2 == 0 && j!=2) {
        continue;
      }
      if(checkPrime(j) && j!=1) {
        cout<<j<<'\n';
      }
    }
    cout<<'\n';
  }
}
