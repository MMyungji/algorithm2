from collections import deque

def dfs(v, visited):
    print(v,end=" ")
    visited[v]=1
    if v in g:
        for next in g[v]:
            if visited[next]==0:
                dfs(next,visited)


def bfs(v):
    visited = [0]*(N+1)
    q = deque([v])
    visited[v]=1
    while q:
        now = q.popleft()
        print(now, end=" ")
        if now not in visited:
            visited.append(now)
        if now in g:
            for next in g[now]:
                if visited[next] == 0:
                    q.append(next)
                    visited[next] = 1


N,M,V = map(int,input().split())
g = {}
for _ in range(M):
    v1,v2 = map(int,input().split())
    if v1 in g: g[v1].append(v2)
    else: g[v1] = [v2]
    if v2 in g: g[v2].append(v1)
    else: g[v2] = [v1]

for i in g:
    g[i].sort()

visited = [0]*(N+1)
dfs(V,visited)
print()
bfs(V)


