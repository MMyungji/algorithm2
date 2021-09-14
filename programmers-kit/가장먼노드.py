from collections import deque


def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])
    print(q)
    while q:
        value = q.popleft()
        print(value)
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                q.append([e, count])


def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)
    bfs(1, visited, adj)
    for dis in visited:
        if dis == max(visited):
            answer += 1
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	))