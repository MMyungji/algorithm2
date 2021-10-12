def dfs(start):
    stack = [start]
    visited = []
    while stack:
        now = stack.pop()
        if now in visited:
            continue
        visited.append(now)
        if graph[now]:
            for i in range(len(graph[now])-1,-1,-1):
                stack.append(graph[now][i])

    return visited

from collections import deque
def bfs(start):
    q = deque([start])
    visited = []
    while q:
        now = q.popleft()
        if now in visited:
            continue
        visited.append(now)
        if graph[now]:
            for i in range(len(graph[now])):
                q.append(graph[now][i])
    return visited


n,m,v = map(int,input().split())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

print(" ".join(map(str,dfs(v))))
print(" ".join(map(str,bfs(v))))
