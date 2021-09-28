# pop(0)보다 popleft()시간복잡도 효율이 좋음
from collections import deque
num = int(input())
q = deque([i for i in range(1,num+1)])
while len(q)>1:
    q.popleft()
    now = q.popleft()
    q.append(now)
print(q[0])

#규칙성
#입력값보다 작은 2의 n제곱의 가장 큰 수를 구하고, 둘의 차이에 2를 곱해주면 된다.
'''
n,m=int(input()),1
while m<n:m*=2
print(n*2-m)
'''