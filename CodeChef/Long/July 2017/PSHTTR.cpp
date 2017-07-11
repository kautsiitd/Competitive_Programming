#include<iostream>
#include<unordered_map>
#include<vector>
#include<tuple>

#define ll long long
using namespace std;

struct pair_hash {
  size_t operator () (const std::pair<int,ll> &p) const {
    auto h1 = std::hash<int>{}(p.first);
    auto h2 = std::hash<ll>{}(p.second);
    return h1 ^ h2;
  }
};

unordered_map<int, vector< pair<int,ll> > >  nodesTree;
unordered_map< pair<int,ll>,ll,pair_hash> xorMap;
unordered_map<int, vector<ll> >  nodeQueryPairs;
tuple<int,int,ll> queries[100005];
bool visited[100005];

struct node {
  node* left;
  node* right;
  ll value, frq, Xor, height;
};

node* createNode(ll value) {
  node *tempNode = new node();
  tempNode->value = value;
  tempNode->frq = 1;
  tempNode->left = NULL;
  tempNode->right = NULL;
  tempNode->Xor = value;
  tempNode->height = 1;
  return tempNode;
}

ll nodeHeight(node* head) {
  if (head == NULL) {
    return 0;
  }
  else {
    return head->height;
  }
}

ll nodeXor(node* head) {
  if (head == NULL) {
    return 0;
  }
  else {
    return head->Xor;
  }
}

node* rightRotate(node* head) {
  node* childNode = head->left;
  // updating pointers first
  head->left = childNode->right;
  childNode->right = head;
  // updating heights
  head->height = max(nodeHeight(head->left), nodeHeight(head->right))+1;
  childNode->height = max(nodeHeight(childNode->left), nodeHeight(childNode->right))+1;
  // updating xor values
  head->Xor = nodeXor(head->left) ^ (head->frq%2 == 0 ? 0:head->value) ^ nodeXor(head->right);
  childNode->Xor = nodeXor(childNode->left) ^ (childNode->frq%2 == 0 ? 0:childNode->value) ^ nodeXor(childNode->right);
  return childNode;
}

node* leftRotate(node* head) {
  node* childNode = head->right;
  // updating pointers first
  head->right = childNode->left;
  childNode->left = head;
  // updating heights
  head->height = max(nodeHeight(head->left), nodeHeight(head->right))+1;
  childNode->height = max(nodeHeight(childNode->left), nodeHeight(childNode->right))+1;
  // updating xor values
  head->Xor = nodeXor(head->left) ^ (head->frq%2 == 0 ? 0:head->value) ^ nodeXor(head->right);
  childNode->Xor = nodeXor(childNode->left) ^ (childNode->frq%2 == 0 ? 0:childNode->value) ^ nodeXor(childNode->right);
  return childNode;
}

ll disBalance(node* head) {
  if (head == NULL) {
    return 0;
  }
  else {
    return nodeHeight(head->left) - nodeHeight(head->right);
  }
}

node* insertValue(ll v, node* head) {
  if (head == NULL) {
    return createNode(v);
  }
  if (v < head->value) {
    head->left = insertValue(v, head->left);
  }
  else if (v > head->value) {
    head->right = insertValue(v, head->right);
  }
  else {
    head->frq += 1;
    head->Xor = nodeXor(head->left) ^ (head->frq%2 == 0 ? 0:head->value) ^ nodeXor(head->right);
    return head;
  }
  // update values
  head->height = max(nodeHeight(head->left), nodeHeight(head->right))+1;
  head->Xor = nodeXor(head->left) ^ (head->frq%2 == 0 ? 0:head->value) ^ nodeXor(head->right);
  // balancing node
  ll balance = disBalance(head);
  // Left Left Case
  if (balance > 1 && v < head->left->value) {
    return rightRotate(head);
  }
  // Right Right Case
  if (balance < -1 && v > head->right->value) {
    return leftRotate(head);
  }
  // Left Right Case
  if (balance > 1 && v > head->left->value) {
      head->left = leftRotate(head->left);
      return rightRotate(head);
  }
  // Right Left Case
  if (balance < -1 && v < head->right->value) {
      head->right = rightRotate(head->right);
      return leftRotate(head);
  }
  return head;
}

node* minValueNode(node* head) {
  node* currentNode = head;
  while(currentNode->left != NULL) {
    currentNode = currentNode->left;
  }
  return currentNode;
}

node* deleteValue(ll v, node* head) {
  if (head == NULL) {
    return head;
  }
  if (v < head->value) {
    head->left = deleteValue(v, head->left);
  }
  else if (v > head->value) {
    head->right = deleteValue(v, head->right);
  }
  else {
    if (head->frq > 1) {
      head->frq -= 1;
      head->Xor = nodeXor(head->left) ^ (head->frq%2 == 0 ? 0:head->value) ^ nodeXor(head->right);
      return head;
    }
    else if (head->left == NULL || head->right == NULL) {
      node* temp = head->left ? head->left : head->right;
      if (temp == NULL) {
        temp = head;
        head = NULL;
      }
      else {
        *head = *temp;
      }
      free(temp);
    }
    else {
      node* temp = minValueNode(head->right);
      head->value = temp->value;
      head->right = deleteValue(temp->value, head->right);
    }
  }
  if (head == NULL) {
    return NULL;
  }
  // updating values
  head->height = max(nodeHeight(head->left), nodeHeight(head->right)) + 1;
  head->Xor = nodeXor(head->left) ^ (head->frq%2 == 0 ? 0:head->value) ^ nodeXor(head->right);
  // balancing tree
  ll balance = disBalance(head);
  // Left Left Case
  if (balance > 1 && disBalance(head->left) >= 0) {
    return rightRotate(head);
  }
  // Left Right Case
  if (balance > 1 && disBalance(head->left) < 0) {
    head->left =  leftRotate(head->left);
    return rightRotate(head);
  }
  // Right Right Case
  if (balance < -1 && disBalance(head->right) <= 0) {
    return leftRotate(head);
  }
  // Right Left Case
  if (balance < -1 && disBalance(head->right) > 0) {
    head->right = rightRotate(head->right);
    return leftRotate(head);
  }
  return head;
}

void preOrder(node* head) {
    if (head != NULL) {
      printf("(%lld %lld)\n", head->value, head->height);
      preOrder(head->left);
      preOrder(head->right);
    }
}

void inOrder(node* head) {
  if (head == NULL) {
    return;
  }
  inOrder(head->left);
  printf("(%lld %lld)\n", head->value, head->height);
  inOrder(head->right);
}

ll findXor(ll value, node* head) {
  if (head == NULL) {
    return 0;
  }
  if (head->value > value) {
    return findXor(value, head->left);
  }
  else if (head->value < value) {
    if (head->left == NULL) {
      return (head->frq%2 == 0 ? 0:head->value) ^ findXor(value, head->right);
    }
    else {
      return head->left->Xor ^ (head->frq%2 == 0 ? 0:head->value) ^ findXor(value, head->right);
    }
  }
  else {
    if (head->left == NULL) {
      return (head->frq%2 == 0 ? 0:head->value);
    }
    else {
      return head->left->Xor ^ (head->frq%2 == 0 ? 0:head->value);
    }
  }
}

node* createXorMap(node* headOfBST,
                  int currentNode) {
    visited[currentNode] = true;
    for (vector< pair<int,ll> >::iterator iter = nodesTree[currentNode].begin();
        iter != nodesTree[currentNode].end();
        ++iter) {
          int nextNodeNumber = iter->first;
          if (visited[nextNodeNumber]) {
            continue;
          }
          ll pathValue = iter->second;
          headOfBST = insertValue(pathValue, headOfBST);
          for (vector<ll>::iterator queryValue = nodeQueryPairs[nextNodeNumber].begin();
              queryValue != nodeQueryPairs[nextNodeNumber].end();
              ++queryValue) {
                xorMap[make_pair(nextNodeNumber,*queryValue)] = findXor(*queryValue,headOfBST);
          }
          headOfBST = createXorMap(headOfBST,
                                  nextNodeNumber);
          headOfBST = deleteValue(pathValue,headOfBST);
    }
    return headOfBST;
}

int main() {
  int t;
  scanf("%d\n", &t);
  for (int _ = 0; _ < t; _++) {
    int n;
    scanf("%d\n", &n);
    // Constructing nodesTree for DFS;
    for (int i = 0; i < n-1; i++) {
      int a,b;
      ll v;
      scanf("%d %d %lld\n", &a, &b, &v);
      if (nodesTree.find(a) == nodesTree.end()) {
        vector< pair<int,ll> > pairs;
        pairs.push_back(make_pair(b,v));
        nodesTree[a] = pairs;
      }
      else {
        nodesTree[a].push_back(make_pair(b,v));
      }
      if (nodesTree.find(b) == nodesTree.end()) {
        vector< pair<int,ll> > pairs;
        pairs.push_back(make_pair(a,v));
        nodesTree[b] = pairs;
      }
      else {
        nodesTree[b].push_back(make_pair(a,v));
      }
    }
    // taking input for queries
    int q;
    scanf("%d\n", &q);
    // storing query values required for various nodes
    for (int i = 0; i < q; i++) {
      int a,b;
      ll v;
      scanf("%d %d %lld\n", &a, &b, &v);
      queries[i] = tuple<int,int,ll>(a,b,v);
      if (nodeQueryPairs.find(a) == nodeQueryPairs.end()) {
        vector<ll> values;
        values.push_back(v);
        nodeQueryPairs[a] = values;
      }
      else {
        nodeQueryPairs[a].push_back(v);
      }
      if (nodeQueryPairs.find(b) == nodeQueryPairs.end()) {
        vector<ll> values;
        values.push_back(v);
        nodeQueryPairs[b] = values;
      }
      else {
        nodeQueryPairs[b].push_back(v);
      }
    }
    // Creating Xor map from root to node using DFS
    for (int i = 0; i < n+1; i++) {
      visited[i] = false;
    }
    node* headOfBST = NULL;
    headOfBST = insertValue(0, headOfBST);
    createXorMap(headOfBST,
                (n+1)/2);
    // solving queries now
    for (int i=0; i<q; i++) {
          tuple<int,int,ll> query = queries[i];
          int nodeA = get<0>(query);
          int nodeB = get<1>(query);
          ll upperValue = get<2>(query);
          printf("%lld\n", (xorMap[make_pair(nodeA,upperValue)] ^ xorMap[make_pair(nodeB,upperValue)]));
        }
    nodesTree.clear();
    xorMap.clear();
    nodeQueryPairs.clear();
  }
  return 0;
}
