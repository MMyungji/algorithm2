N = int(input())
condo = [list(input()) for _ in range(N)]
garo,sero = 0,0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N-1):
        if visited[i][j] == 0 and condo[i][j] == '.':
            if condo[i][j + 1] == '.':
                garo += 1
                for k in range(j, N):
                    if condo[i][k] == 'X': break
                    visited[i][k] = 1

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N-1):
        if visited[j][i] == 0 and condo[j][i] == '.':
            if condo[j+1][i] == '.':
                sero += 1
                for k in range(j, N):
                    if condo[k][i] == 'X': break
                    visited[k][i] = 1
print(garo, sero)