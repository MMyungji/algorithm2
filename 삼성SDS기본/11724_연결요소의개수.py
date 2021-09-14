def bfs(v):
    q = [v]
    while q:
        v = q.pop(0)
        for i in range(1,N+1):
            if data[i][v]==1 and visited[i]==0:
                visited[i]=1
                q.append(i)

N,M = map(int,input().split())
data = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    data[i][j] = data[j][i] = 1

visited = [0]*(N+1)
count=0
for i in range(1,N+1):
    if visited[i]==0:
        bfs(i)
        count+=1
print(count)