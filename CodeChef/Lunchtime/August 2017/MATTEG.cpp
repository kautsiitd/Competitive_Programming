#include<bits/stdc++.h>
using namespace std;
#define ll long long

int r,c,n;
ll ans;
bool visited[10];
ll valueBoard[1005][1005];
int moves[10][2];

void findAns(int cx, int cy, ll tempAns, int doneVisited) {
	ans = max(tempAns,ans);
	if(doneVisited == n || cx<0 || cx>r || cy<0 || cy>c) {
		return;
	}
	else {
		for(int i=0;i<n;i++) {
			if(visited[i]) {
				continue;
			}
			else {
				visited[i] = true;
				int newCx,newCy;
				newCx = cx+moves[i][0];
        newCy = cy+moves[i][1];
				if(newCx>=0 && newCx<r && newCy>=0 && newCy<c) {
					findAns(newCx,newCy,tempAns+valueBoard[newCx][newCy],doneVisited+1);
				}
				newCx = cx+moves[i][0];
        newCy = cy-moves[i][1];
				if(newCx>=0 && newCx<r && newCy>=0 && newCy<c) {
					findAns(newCx,newCy,tempAns+valueBoard[newCx][newCy],doneVisited+1);
				}
				newCx = cx-moves[i][0];
        newCy = cy+moves[i][1];
				if(newCx>=0 && newCx<r && newCy>=0 && newCy<c) {
					findAns(newCx,newCy,tempAns+valueBoard[newCx][newCy],doneVisited+1);
				}
				newCx = cx-moves[i][0];
        newCy = cy-moves[i][1];
				if(newCx>=0 && newCx<r && newCy>=0 && newCy<c) {
					findAns(newCx,newCy,tempAns+valueBoard[newCx][newCy],doneVisited+1);
				}
				visited[i] = false;
			}
		}
	}
}

int main() {
	int t;
	scanf("%d\n",&t);
	for (int _ = 0; _ < t; _++) {
		scanf("%d %d %d\n",&r,&c,&n);
		int sx,sy;
		scanf("%d %d\n",&sx,&sy);
		for (int i = 0; i < n-1; i++) {
			scanf("%d ",&moves[i][0]);
		}
		scanf("%d\n",&moves[n-1][0]);
		for (int i = 0; i < n-1; i++) {
			scanf("%d ",&moves[i][1]);
		}
		scanf("%d\n",&moves[n-1][1]);
		for(int i=0;i<r;i++) {
			for (int j=0;j<c-1;j++) {
				scanf("%lld ",&valueBoard[i][j]);
			}
			scanf("%lld\n",&valueBoard[i][c-1]);
		}
		for(int i=0;i<n;i++) {
			visited[i] = false;
		}
		ans = 0;
		findAns(sx,sy,0,0);
		printf("%lld\n",ans+valueBoard[sx][sy]);
	}
	return 0;
}
