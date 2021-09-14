nums = list(map(int,input().split()))
res = 0
for num in nums:
    res+=num**2
print(res%10)