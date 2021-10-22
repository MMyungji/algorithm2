# 시뮬레이션 - 꼭 BFS, DFS 안써도 된다
# 적당한 while, for문으로 구현 가능

direction={
    1:[-1,0],
    2:[1,0],
    3:[0,-1],
    4:[0,1]
}

N,M,K = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)] # 지도
dir=[[[0]*4 for _ in range(5)] for _ in range(1+M)]     #이동방향 우선순위데이터 dir[상어번호][현재 방향] = [0,0,0,0]
shark=[0 for _ in range(M+1)]       # 상어위치
shark_dir=[0]+list(map(int,input().split()))    #상어현재 이동방향
visited=[[0 for _ in range(N)] for _ in range(N)]       #현재 위치에 상어 숫자와 냄새 저장, 몇초에 도착했는지

def is_safe(a,b):
    return 0<=a<N and 0<=b<N

# 냄새 사라지기
def smell():
    global visited
    for i in range(N):
        for j in range(N):
            if visited[i][j]!=0:
                visited[i][j][1]-=1
                if visited[i][j][1]==0:
                    visited[i][j] = 0

def last_shark():
    cnt=[]
    for i in range(1,1+M):
        if shark[i] == 0:
            cnt.append(i)
    return len(cnt)

# 상어 이동하기
def move():
    global visited
    ans=0
    while True:
        # print("\n".join(map(str, visited)))
        ans+=1
        if ans == 1001:
            return -1

        check = [[0]*N for _ in range(N)] #현재 상어위치 확인

        for number in range(1,M+1):
            if shark[number]==0: continue
            y,x = shark[number]
            d = shark_dir[number]
            flag=0
            for j in range(4):
                nd = dir[number][d][j]
                ny,nx = y+direction[nd][0], x+direction[nd][1]
                if is_safe(ny,nx):
                    if visited[ny][nx]==0:
                        flag=1
                        break

            if flag==0:
                for j in range(4):
                    nd = dir[number][shark_dir[number]][j]
                    ny, nx = y + direction[nd][0], x + direction[nd][1]
                    if is_safe(ny, nx):
                        if visited[ny][nx][0] == number:
                            break

            if check[ny][nx]:
                if check[ny][nx]<number:
                    shark[number]=0
                else:
                    shark[check[ny][nx]]=0
            else:
                check[ny][nx]=number
                shark[number]=[ny,nx]
                shark_dir[number]= nd

        # for i in range(N):
        #     for j in range(N):
        #         if visited[i][j]:
        #             visited[i][j][1]-=1
        #             if visited[i][j][1]==0:
        #                 visited[i][j]=0
        smell()

        for i in range(1,1+M):
            if shark[i]:
                y,x = shark[i]
                visited[y][x]=[i,K]
        # if shark.count(0)==M-1:
        #     return ans

        if last_shark()==M-1:
            return ans

# 상어 이동방향 우선순위 데이터 저장
for i in range(1,M+1):
    for j in range(1,5):
        dir[i][j]=list(map(int,input().split()))

# 상어 시작 위치 저장
for i in range(N):
    for j in range(N):
        if data[i][j]!=0:
            shark[data[i][j]] = [i,j]
            visited[i][j] = [data[i][j],K] # 상어번호, 초, 몇초에 왔는지

print(move())