nums = [int(input()) for _ in range(3)]
res = 1
for num in nums:
    res*=num

ans=[0]*10
for n in str(res):
    ans[int(n)]+=1
for n in ans:
    print(n)