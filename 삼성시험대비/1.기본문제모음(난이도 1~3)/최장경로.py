# dfs(재귀), 백트래킹
def dfs(idx,cnt):
    global max_cnt
    for i in range(1, N+1):
        if data[idx][i] == 1 and visited[i]==0:
            visited[i]=1
            dfs(i,cnt+1)
            visited[i]=0
        else:
            max_cnt = max(cnt,max_cnt)

for tc in range(int(input())):
    N,M = map(int,input().split())
    data = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        data[a][b]=1
        data[b][a]=1

    visited = [0] * (N + 1)
    max_cnt = 0

    for i in range(1,N+1):
        visited[i]=1
        dfs(i,1)
        visited[i]=0

    print("#{} {}".format(tc+1, max_cnt))
