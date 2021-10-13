def password(nums,start):
    while True:
        if nums[start]!=nums[start+1]:
            break
        del nums[start+1]
        del nums[start]
        if start < len(nums):
            start-=1
        else:
            break
    return nums

def is_ok(nums):
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return i
    return -1
for tc in range(1,11):
    N, data = input().split()
    N = int(N) 
    data = list(map(int,data))
    start=is_ok(data)
    while start!=-1:
        # print(data,start)
        data = password(data,start)
        start=is_ok(data)
    print(f"#{tc} {''.join(map(str,data))}")