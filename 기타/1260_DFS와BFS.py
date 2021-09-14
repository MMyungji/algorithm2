from collections import deque

def dfs(g,v):
    visited = []
    stack = [v]
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
        if now in g:
            now_list = sorted(g[now], reverse=True)
            for node in now_list:
                if node in visited: continue
                stack.append(node)

    return visited

def bfs(g,v):
    visited = []
    q = deque([v])
    while q:
        now = q.popleft()
        if now not in visited:
            visited.append(now)
        if now in g:
            now_list = sorted(g[now])
            for node in now_list:
                if node in visited or node in q: continue
                q.append(node)

    return visited

N,M,V = map(int,input().split())
g = {}
for _ in range(M):
    v1,v2 = map(int,input().split())
    if v1 in g: g[v1].append(v2)
    else: g[v1] = [v2]
    if v2 in g: g[v2].append(v1)
    else: g[v2] = [v1]


res1 = " ".join(map(str,dfs(g,V)))
res2 = " ".join(map(str,bfs(g,V)))
print(res1)
print(res2)


