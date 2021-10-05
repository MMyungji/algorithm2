# N,M = map(int,input().split())
# trees = list(map(int,input().split()))

import sys
N,M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
left,right = 1,max(trees)
while left<=right:
    mid = (left+right)//2
    res = 0
    for tree in trees:
        if tree>=mid:
            res+=tree-mid
    if res < M:
        right=mid-1
    else:
        left=mid+1
print(right)