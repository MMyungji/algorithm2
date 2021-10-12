#dp-(배열의) 누적합, 시간초과(구현, 큐)
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + arr[i][j]
for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    res = dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1]) + dp[x1-1][y1-1]
    print(res)

# N,M = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# for _ in range(M):
#     x1,y1,x2,y2 = map(int,input().split())
#     res = 0
#     for r in range(x1-1,x2):
#         for c in range(y1-1,y2):
#             res+=arr[r][c]
#     print(res)

# from collections import deque
# dir = [[0,1],[1,0]]
# N,M = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# for _ in range(M):
#     x1,y1,x2,y2 = map(int,input().split())
#     res = 0
#     q = deque([[x1-1,y1-1]])
#     visited = [[0]*N for _ in range(N)]
#     while q:
#         x,y = q.popleft()
#         # print(1,x,y,arr[x][y],res+arr[x][y])
#         res+=arr[x][y]
#         visited[x][y]=1
#         for dx,dy in dir:
#             nx = x+dx
#             ny = y+dy
#             # print(2,nx,ny)
#             if x1-1<=nx<=x2-1 and y1-1<=ny<=y2-1:
#                 if visited[nx][ny] == 1 or [nx,ny] in q:
#                     continue
#                 q.append([nx,ny])
#     print(res)


