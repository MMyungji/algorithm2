# 큐에선 deque를 써주는 것이 좋음

from collections import deque

for _ in range(int(input())):
    N,M = map(int,input().split())
    importance = list(map(int,input().split()))
    impt = [-1]+sorted(importance,reverse=True)
    q = deque()
    for i in range(N):
        q.append([i,importance[i]])
    # print(q)
    cnt=1
    while q:
        now = q.popleft()
        # print(now, impt[cnt])
        if now[1]!=impt[cnt]:
            q.append(now)
        else:
            if now[0]==M:
                print(cnt)
                break
            else:
                q.append(now)
                cnt += 1
'''
from collections import deque 
t = int(input()) 
for _ in range(t):
    n , x = map(int,input().split())
    que = deque(list(map(int,input().split())))
    idx_que = deque(list(range(n)))
    cnt = 0 
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            if idx_que.popleft() == x:
                print(cnt)
        else:
            que.append(que.popleft())
            idx_que.append(idx_que.popleft())
'''


