# 시뮬레이션, 브루트포스
N,M = map(int,input().split())
data = [list(input()) for _ in range(N)]
res = []
for i in range(N-8+1):
    for j in range(M-8+1):
        white, black = 0,0 #흰색 또는 검은색으로 시작할 때
        for r in range(i,i+8):
            for c in range(j,j+8):
                if (r+c)%2==0: #번갈아가면서 색이 다른지 확인
                    if data[r][c] != "W":
                        white+=1
                    if data[r][c] != "B":
                        black+=1
                else:
                    if data[r][c] != "B":
                        white+=1
                    if data[r][c] != "W":
                        black+=1

        res.extend([white,black])

print(min(res))

