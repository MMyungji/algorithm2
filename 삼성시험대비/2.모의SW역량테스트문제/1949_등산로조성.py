dir = [(0,1),(0,-1),(1,0),(-1,0)]
def is_ok(x,y):
    return 0<=x<N and 0<=y<N

def make(x,y,cnt,flag):
    global res
    if cnt>res:
        # print("====")
        # print(f"cnt:{cnt}, flag:{flag}")
        # print("\n".join(map(str,data)))
        # print()
        # print("\n".join(map(str,visited)))
        # print("====")
        res=cnt

    for dx,dy in dir:
        nx=x+dx
        ny=y+dy
        if is_ok(nx,ny):
            if visited[nx][ny]==0:
                if data[nx][ny]<data[x][y]:
                    visited[nx][ny] = 1
                    make(nx,ny,cnt+1,flag)
                    visited[nx][ny]=0
                else:
                    if flag and data[nx][ny]-K<=data[x][y]-1:
                        pre = data[nx][ny]
                        data[nx][ny] = data[x][y]-1
                        visited[nx][ny]=1
                        make(nx,ny,cnt+1,False)
                        data[nx][ny]=pre
                        visited[nx][ny]=0

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    res=0

    max_highs=[]
    max_high=0
    for i in range(N):
        for j in range(N):
            if max_high<data[i][j]:
                max_highs.clear()
                max_high=data[i][j]
                max_highs.append((i,j))
            elif max_high==data[i][j]:
                max_highs.append((i, j))


    for i,j in max_highs:
        visited = [[0] * N for _ in range(N)]
        visited[i][j]=1
        make(i,j,1,True)

    print(f"#{tc} {res}")


'''
# 예전코드
dir = [(1,0),(-1,0),(0,1),(0,-1)]
def isSafe(y,x):
    return 0<=y<N and 0<=x<N

# dfs
def make_road(y,x,k,cnt):
    global road
    now_h = mountain[y][x]
    for di,dj in dir:
        ny = y+di
        nx = x+dj
        if not isSafe(ny,nx):
            continue
        if visited[ny][nx]:
            continue
        
        next_h = mountain[ny][nx]
        if next_h<now_h: # 현재 봉우리 높이보다 작으면 재귀
            visited[ny][nx] = 1
            make_road(ny,nx,k,cnt+1)
            visited[ny][nx] = 0
        else:
            if k>0 and next_h-k<now_h: # K(지형을 깎는 공사)를 사용하지 않았고, 공사 후에 현재 봉우리보다 낮은 봉우리 재귀
                visited[ny][nx] = 1
                temp = mountain[ny][nx] # 산 봉우리 높이 조정하기
                mountain[ny][nx] = now_h-1
                make_road(ny, nx, 0, cnt+1)
                mountain[ny][nx] = temp
                visited[ny][nx] = 0
            else:
                # 다음 봉우리가 현재 봉우리보다 크면 STOP
                # road = max(road, cnt)
                if road<cnt:
                    road=cnt
                    # print(f"MAX: {road}")
                    # print(f"last y,x,k: {y,x,k}")
                    # print(f"now:{now_h}, next:{next_h}")
                    # print("mountain")
                    # for m in mountain:
                    #     print(*m)
                    # print("visited")
                    # for v in visited:
                    #     print(v)


for testcase in range(1,1+int(input())):
    N,Kk = map(int,input().split())
    mountain = [list(map(int,input().split())) for _ in range(N)]

    # 제일 높은 봉우리의 높이와 리스트 찾기
    max_heights = []
    height = 0

    for i in range(N):
        for j in range(N):
            if height<mountain[i][j]:
                max_heights = [(i,j)]
                height = mountain[i][j]
            elif height==mountain[i][j]:
                max_heights.append((i,j))

    road = 0 # 가장 긴 등산로
    for h in max_heights:
        visited = [[0] * N for _ in range(N)] # 방문 봉우리 리셋
        visited[h[0]][h[1]] = 1
        make_road(h[0],h[1],Kk,1)

    print(f"#{testcase} {road}")
'''