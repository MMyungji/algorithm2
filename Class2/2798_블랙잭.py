N,M = map(int,input().split())
data = list(map(int,input().split()))
res = 0
'''
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if data[i]+data[j]+data[k] > M:
                continue
            res = max(res,data[i]+data[j]+data[k])
print(res)
'''

from itertools import combinations as cb
for selected in cb(data,3):
    sum_selected = sum(selected)
    if sum_selected>M:
        continue
    res = max(res, sum_selected)
print(res)
