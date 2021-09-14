# 1. 트리형태 ( 사용 O, X) - brunch 수, level 수 명확
# 2. 가지치기 (used, map 확인)

'''
(모든 경우 다 확인해야 하는 경우의 문제)
1. 백트래킹 - 재귀 (1. 가지치기, 2. 트리형태, 3. DP 요소 발굴)

2. 완탐 - for, 재귀
(easy - 재귀 구현, 가지치기 단순 하나, for문 필요X / 완탐에 알고리즘)
(mid - 가지치기 조건 싹 다 넣기)
(hard - 가지치기 조건 + DP)

3. DFS - 그래프
'''
def setNemo(y,x):
    global used
    used[y][x] = 2
    used[y][x + 1] = 1
    used[y + 1][x] = 1
    used[y + 1][x + 1] = 1

def isClean(dy,dx):
    global used, wiper
    if dx >= W-1: return 0
    if wiper[dy][dx] + wiper[dy][dx + 1] + wiper[dy + 1][dx] + wiper[dy + 1][dx + 1] > 0: return False
    if used[dy][dx]+used[dy][dx+1]+used[dy+1][dx]+used[dy+1][dx+1] > 0 : return False
    return True

def clearNemo(y, x):
    global used
    used[y][x] = 0
    used[y][x + 1] = 0
    used[y + 1][x] = 0
    used[y + 1][x + 1] = 0

def getState(y, x):
    state = 0
    for i in range(W-1):
        state <<= 1
        if used[y][i] == 2 : state |= 0x1
        return state

def getMaxChipCnt(stage):
    global memo
    dy = int(stage / W)
    dx = int(stage % W)

    if dy==H-2 and dx==W-1: return 0
    if dx == W-1:
        state = getState(dy,dx)
        if memo[dy][state] != 0: return memo[dy][state]

    maxCount = 0
    # 네모 설치
    if isClean(dy,dx):
        setNemo(dy,dx)
        result = getMaxChipCnt(stage+1)+1
        clearNemo(dy,dx)

    # 네모 설치안함
    result = getMaxChipCnt(stage+1)
    if result>maxCount: maxCount=result

    if dx == W-1:
        memo[dy][state] = maxCount

    return maxCount


for tc in range(int(input())):
    H,W = map(int,input().split())
    wiper = [list(map(int,input().split())) for _ in range(H)]
    used = [[0]*W for _ in range(H)]
    memo = [[0]*H for _ in range(W)]

    result = getMaxChipCnt(0)


    print("#{} {}".format(tc+1, result))
