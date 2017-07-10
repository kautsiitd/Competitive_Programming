#include<iostream>

#define ll long long
using namespace std;

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
    return NULL;
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
      return head;
    }
    else if (head->left == NULL || head->right == NULL) {
      node* temp = head->left ? head->left : head->right;
      if (temp == NULL) {
        head = NULL;
      }
      else {
        head = temp;
        free(temp);
      }
    }
    else {
      node* temp = minValueNode(head->right);
      head->value = temp->value;
      head->right = deleteValue(temp->value, head->right);
    }
  }

  if (head == NULL) {
    return head;
  }
  // updating values
  head->height = max(nodeHeight(head->left), nodeHeight(head->right)) + 1;
  head->Xor = nodeXor(head->left) ^ head->value ^ nodeXor(head->right);
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
        cout<<head->value<<head->height<<" ";
        preOrder(head->left);
        preOrder(head->right);
    }
}

void inOrder(node* head) {
  if (head == NULL) {
    return;
  }
  inOrder(head->left);
  cout<<head->value<<" ";
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
      return head->value ^ findXor(value, head->right);
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

int main() {
  node* head = NULL;
  head = insertValue(7, head);
  head = insertValue(3, head);
  head = insertValue(8, head);
  head = insertValue(1, head);
  head = insertValue(5, head);
  head = insertValue(3, head);
  head = insertValue(2, head);
  head = insertValue(4, head);
  head = deleteValue(2, head);
  head = insertValue(2, head);
  head = insertValue(9, head);
  head = deleteValue(4, head);
  head = insertValue(7, head);
  head = deleteValue(7, head);
  head = deleteValue(9, head);
  preOrder(head);
  cout<<'\n';
  inOrder(head);
  cout<<'\n';
  while (true) {
    ll v;
    cin>>v;
    cout<<findXor(v, head);
    cout<<'\n';
  }
}
