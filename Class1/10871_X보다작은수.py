N,X = map(int,input().split())
nums = list(map(int,input().split()))
res = []
for i in range(N):
    if nums[i]<X:
        res.append(nums[i])
print(" ".join(map(str,res)))