dir = [[1,0],[0,1],[1,1]]
def isOK(x,y):
    return 0<=x<H and 0<=y<W

def solution(x,y):
    global visited
    visited[x][y] = 1
    flag = True
    for dx,dy in dir:
        nx = x+dx
        ny = y+dy
        if isOK(nx,ny):
            if wiper[nx][ny] == 1 or visited[nx][ny] == 1:
                flag = False
                break
        else:
            flag = False
            break
    if flag:
        visited[x][y] = 1
        for dx,dy in dir:
            nx = x + dx
            ny = y + dy
            visited[nx][ny] = 1
        return 1
    else:
        return 0


for tc in range(int(input())):
    H,W = map(int,input().split())
    wiper = [list(map(int,input().split())) for _ in range(H)]
    visited = [[0]*W for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if wiper[i][j]==0 and visited[i][j]==0:
                count += solution(i,j)
    print("#{} {}".format(tc+1, count))
