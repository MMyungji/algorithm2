# heapq - 시간초과(간선끼리의 가중치가 있을 경우 사용하는 최단거리 구하기)
# deque(bfs) -> distance 계산 배열 생성 -> 거리+1 (가중치없을땐, bfs에서 distance누적하는 리스트만들어서 계산)

from collections import deque
dir = [[1,0],[0,1],[0,-1],[-1,0]]
def bfs():
    q = deque([[0,0]])
    distance = [[0]*m for _ in range(n)]
    distance[0][0]=1
    while q:
        x,y = q.popleft()
        if x==n-1 and y==m-1:
            # for d in distance:
            #     print(" ".join(map(str,d)))
            return distance[n-1][m-1]
        for dx,dy in dir:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                if miro[nx][ny]=="1" and distance[nx][ny]==0:
                    distance[nx][ny]=distance[x][y]+1
                    q.append([nx,ny])


n,m = map(int,input().split())
miro = [input() for _ in range(n)]
print(bfs())


# 시간초과
# from heapq import heappush, heappop
# import sys
# input = sys.stdin.readline
# dir = [[1,0],[0,1],[0,-1],[-1,0]]
# def bfs():
#     q=[[1,[0,0]]]
#     visited = [[0]*m for _ in range(n)]
#     while q:
#         cnt,[x,y] = heappop(q)
#         visited[x][y]=1
#         if x==n-1 and y==m-1:
#             print(cnt)
#             # for i in visited:
#             #     print(" ".join(map(str,i)))
#             break
#         for dx,dy in dir:
#             nx=x+dx
#             ny=y+dy
#             if 0<=nx<n and 0<=ny<m:
#                 if miro[nx][ny]=="1":
#                     if visited[nx][ny]==0:
#                         heappush(q,[cnt+1,[nx,ny]])
#
# n,m = map(int,input().split())
# miro = [input() for _ in range(n)]
# bfs()
#
