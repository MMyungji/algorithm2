dir = [(1,0),(0,-1),(-1,0),(0,1)]
def is_safe(a,b):
    return 0<=a<N and 0<=b<N

def delete_dfs(g):
    global total
    cnt=0
    for x,y in g:
        data[x][y]=-2
        cnt+=1
    total+=cnt**2

def size_dfs(a,b):
    global visited
    stack = [[a,b]]
    num = data[a][b]
    group = [[a,b]]
    while stack:
        x,y = stack.pop()
        for dx,dy in dir:
            nx,ny=x+dx,y+dy
            if not is_safe(nx,ny):
                continue
            if data[nx][ny]==num:
                if visited[nx][ny]:
                    continue
                if [nx,ny] not in group:
                    group.append([nx,ny])
                    stack.append([nx,ny])
                    visited[nx][ny]=1
            if data[nx][ny]==0:
                if [nx,ny] not in group:
                    group.append([nx,ny])
                    stack.append([nx,ny])
    return sorted(group)

def gravity():
    for j in range(N):
        start,idx = N-1,N
        move_idx=[]
        while True:
            idx-=1
            if idx==-1:
                break
            if idx==start and data[idx][j]>=0:
                start-=1
            elif data[idx][j]==-2:
                if start <= idx:
                    start=idx
            elif data[idx][j]==-1:
                for k in range(len(move_idx)):
                    data[start-k][j],data[move_idx[k]][j]=data[move_idx[k]][j],data[start-k][j]
                move_idx=[]
                start = idx-1
            else:
                move_idx.append(idx)
        if move_idx:
            for k in range(len(move_idx)):
                data[start - k][j], data[move_idx[k]][j] = data[move_idx[k]][j], data[start - k][j]



N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
total = 0
while True:
    # 블록 그룹 - 크기가 큰것 구하
    visited = [[0]*N for _ in range(N)]
    groups=[]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0 and 1<=data[i][j]<=M:
                lst = size_dfs(i,j)
                if len(lst)>1:
                    if groups:
                        if len(groups[0])<len(lst):
                            groups = [lst]
                        elif len(groups[0])==len(lst):
                            groups.append(lst)
                    else:
                        groups = [lst]

    if groups==[]:
        break

    who_is_big = []
    if len(groups)==1:
        who_is_big = groups[0]
    else:
    # 가장 큰 그룹 찾기 1. 무지개수 비교 / 2. 행 큰것 / 3. 열 큰것

        rainbow_max=0
        for g in groups: # 무지개 큰것
            r_cnt = 0
            for i,j in g:
                if data[i][j]==0:
                    r_cnt+=1
            if r_cnt>rainbow_max:
                who_is_big=[g]
                rainbow_max=r_cnt
            if r_cnt==rainbow_max:
                who_is_big.append(g)

        row_max=[]
        max_idx=-1
        if len(who_is_big)>1: # 행 큰것 / 열 큰것 비교
            for g in range(len(who_is_big)):
                r,c = who_is_big[g][-1]
                if row_max==[]:
                    row_max.append([r,c,g])
                    continue
                if r>row_max[0][0]:
                    row_max=[[r,c,g]]
                elif r==row_max[0][0]:
                    row_max.append([r,c,g])
            if len(row_max)==1:
                who_is_big = who_is_big[row_max[0][2]]
            else:
                row_max.sort()
                who_is_big = who_is_big[row_max[-1][2]]

    delete_dfs(who_is_big)
    # print("\n".join(map(str,data)))
    gravity()
    # print("\n".join(map(str,data)))
    data = [list(row) for row in list(zip(*data))[::-1]]
    gravity()
    # print("\n".join(map(str,data)))

print(total)