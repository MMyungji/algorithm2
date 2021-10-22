# import itertools
dir = [(1,0),(0,1),(-1,0),(0,-1)]
def is_safe(x,y):
    return 0<=x<N and 0<=y<N

def calc():
    total=0
    for i in range(N):
        for j in range(N):
            num = data[i][j]
            cnt=0
            friends = friend_data[num]
            for di,dj in dir:
                ni = i+di
                nj = j+dj
                if is_safe(ni,nj):
                    if data[ni][nj] in friends:
                        cnt+=1
            if cnt>0:
                total+=10**(cnt-1)
    return total
N = int(input())
data = [[0]*N for _ in range(N)]
friend_data = [[] for _ in range(N*N+1)]
for i in range(N*N):
    num, n1,n2,n3,n4 = map(int,input().split()) # 자신과 친한 상어들
    friends = [n1,n2,n3,n4]
    friend_data[num] = friends
    # now = list(itertools.chain(*data))
    # 맨 처음
    if i==0:
        data[1][1]=num
        continue

    # 1번째 조건: 좋아하는 학생 인접
    is_bf = []
    for n in friends:
        for i in range(N):
            for j in range(N):
                if data[i][j]==n:
                    is_bf.append([i,j])
                    break
    is_close = [] #친한 친구와 가까운 곳
    bf_cnt=0
    for tx in range(N):
        for ty in range(N):
            if data[tx][ty]==0:
                cnt=0
                for x,y in is_bf:
                    if abs(tx-x)+abs(ty-y)==1:
                        cnt+=1
                if cnt>bf_cnt:
                    bf_cnt=cnt
                    is_close = [[tx,ty]]
                elif cnt==bf_cnt:
                    is_close.append([tx,ty])

    # print("친구가 제일 많은 곳 {}".format(is_close))
    if len(is_close)==1:
        x,y = is_close[0]
        data[x][y]=num
        continue

    is_empty=[]
    max_empty=0
    for x,y in is_close:
        empty_cnt=0
        for dx,dy in dir:
            nx=x+dx
            ny=y+dy
            if is_safe(nx,ny):
                if data[nx][ny]==0:
                    empty_cnt+=1
        if empty_cnt>max_empty:
            max_empty=empty_cnt
            is_empty = [[x,y]]
        elif empty_cnt==max_empty:
            is_empty.append([x,y])

    # print("주변에 가장 빈곳이 많은데: {}".format(is_empty))
    if len(is_empty)==1:
        x,y = is_empty[0]
        data[x][y] = num
        continue

    is_empty.sort()
    min_row = [] #가장 행이 작은것

    for xi,yi in is_empty:
        if min_row==[]:
            min_row = [[xi,yi]]
        elif min_row[0][0] == xi:
            min_row.append([xi,yi])
        elif min_row[0][0]>xi:
            min_row = [[xi,yi]]
    # print("행 작은 것 -> {}".format(min_row))
    if len(min_row)==1:
        rx,ry = min_row[0]
        data[rx][ry]=num
        continue

    min_col = []
    for ti,tj in min_row:
        if min_col==[]:
            min_col=[[ti,tj]]
        elif min_col[0][1]==tj:
            min_col.append([ti,tj])
        elif min_col[0][1]>tj:
            min_col=[[ti,tj]]
    min_col.sort()
    # print("열 작은 것 -> {}".format(min_col))
    lx,ly = min_col[0]
    data[lx][ly]=num
    continue

# print("\n".join(map(str,data)))
total = calc()
print(total)










