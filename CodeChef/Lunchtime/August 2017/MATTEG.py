def findAns(cx,cy,tempAns,doneVisited):
    global ans
    ans = max(tempAns,ans)
    if doneVisited == n or cx<0 or cx>r or cy<0 or cy>c:
        return
    else:
        for i in range(n):
            if visited[i]:
                continue
            else:
                visited[i] = True
                newCx = cx+moves[i][0]
                newCy = cy+moves[i][1]
                if newCx>=0 and newCx<r and newCy>=0 and newCy<c:
                    findAns(newCx,newCy,tempAns+valueBoard[newCx][newCy],doneVisited+1)
                newCx = cx-moves[i][0]
                newCy = cy+moves[i][1]
                if newCx>=0 and newCx<r and newCy>=0 and newCy<c:
                    findAns(newCx,newCy,tempAns+valueBoard[newCx][newCy],doneVisited+1)
                newCx = cx+moves[i][0]
                newCy = cy-moves[i][1]
                if newCx>=0 and newCx<r and newCy>=0 and newCy<c:
                    findAns(newCx,newCy,tempAns+valueBoard[newCx][newCy],doneVisited+1)
                newCx = cx-moves[i][0]
                newCy = cy-moves[i][1]
                if newCx>=0 and newCx<r and newCy>=0 and newCy<c:
                    findAns(newCx,newCy,tempAns+valueBoard[newCx][newCy],doneVisited+1)
                visited[i] = False

for _ in range(input()):
    r,c,n = map(int,raw_input().split())
    sx,sy = map(int,raw_input().split())
    x = map(int,raw_input().split())
    y = map(int,raw_input().split())
    moves = zip(x,y)
    valueBoard = [map(int,raw_input().split()) for __ in range(r)]
    visited = [False for i in range(n)]
    ans = 0
    findAns(sx,sy,0,0)
    print ans+valueBoard[sx][sy]
