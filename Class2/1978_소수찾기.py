# 소수찾기 - for문 2개
N = int(input())
nums = list(map(int,input().split()))
a = [False,False]+[True]*(max(nums)-1)
cnt = 0
for i in range(2,max(nums)+1):
    if a[i]:
        if i in nums:
            cnt+=1
        for j in range(i*2,max(nums)+1,i):
            a[j]=False
print(cnt)