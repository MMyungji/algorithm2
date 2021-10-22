dir=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
import copy
def is_safe(x,y):
    return 0<=x<4 and 0<=y<4
# 물고기 이동
def fish_move(sx,sy):
    for num in range(16): # 물고기 번호 작은거부터
        if fish_data[num]==[]:
            continue
        x,y = fish_data[num]
        for _ in range(9): # 9번 움직임 (원래 방향으로 돌아오면 움직이지 않는다)
            nx,ny = x+dir[mat[x][y][1]][0], y+dir[mat[x][y][1]][1]
            if not is_safe(nx,ny) or (nx==sx and ny==sy):
                mat[x][y][1] = (mat[x][y][1]+1)%8
                continue
            if mat[nx][ny]:
                fish_data[mat[nx][ny][0]]=[x,y] #물고기 위치 바뀔때
            mat[nx][ny], mat[x][y] = mat[x][y], mat[nx][ny]
            fish_data[num] = [nx,ny]
            break


def shark_move(x,y,d,cnt): # 상어 위치, 방향,합계
    global ans,fish_data,mat
    # 물고기 이동
    fish_move(x,y)
    # 상어 이동하면서 물고기 잡아먹고 재귀 부르기 + 원상태 복귀
    while True:
        nx,ny = x+dir[d][0], y+dir[d][1]
        if not is_safe(nx,ny): #상어 이탈 -> 최대 확인
            ans = max(ans,cnt)
            return
        if not mat[nx][ny]: # 물고기 없으면 이동 경로로만 사용
            x,y=nx,ny
            continue
        temp_mat, temp_fish = copy.deepcopy(mat), copy.deepcopy(fish_data) #이동전 데이터 저장
        temp_1 = mat[nx][ny] # 기존의 해당 위치의 물고기 데이터
        temp_2 = fish_data[mat[nx][ny][0]] #그 물고기의 위치

        fish_data[mat[nx][ny][0]] = [] #잡아 먹은 물고기 데이터 삭제
        mat[nx][ny] = []
        shark_move(nx,ny,temp_1[1],cnt+temp_1[0]+1) # 재귀

        mat, fish_data = temp_mat, temp_fish # 이동전 데이터 복귀
        # mat[nx][ny] = temp_1
        # fish_data[mat[nx][ny][0]]=temp_2
        x,y=nx,ny # 이동하면서 확인



mat = [[0]*4 for _ in range(4)]
fish_data=[0]*16
for i in range(4):
    temp = list(map(int,input().split()))
    for j in range(0,8,2):
        num,d=temp[j:j+2]
        mat[i][j//2] = [num-1,d-1]
        fish_data[num-1]=[i,j//2] # 물고기 데이터에는 x,y좌표

# 상어 (0,0) 먹고 -> 해당 물고기 방향 갖는다
num,d = mat[0][0]
fish_data[num]=[]
mat[0][0] = []
ans=num+1
# print(mat)
# print(fish_data)
shark_move(0,0,d,ans)
print(ans)
