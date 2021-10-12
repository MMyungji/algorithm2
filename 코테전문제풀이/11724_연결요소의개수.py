# 그래프 구현 + 그래프 탐색
# dfs - visited와 stack을 한번에 -> 변수명 확인하기

import sys
input = sys.stdin.readline

def dfs(start):
    global visited
    stack = [start]
    while stack:
        now = stack.pop()
        for i in range(1,N+1):
            if graph[now][i]==1 and visited[i]==0:
                visited[i] = 1
                stack.append(i)

N,M = map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u][v]=1
    graph[v][u]=1

visited = [0]*(N+1)
cnt=0
for i in range(1,N+1):
    if visited[i]==0:
        dfs(i)
        cnt+=1
print(cnt)