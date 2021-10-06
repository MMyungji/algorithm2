while True:
    nums = list(map(int,input().split()))
    if nums == [0,0,0]:
        break
    max_idx = nums.index(max(nums))
    left = 0
    for i in range(3):
        if max_idx==i:
            continue
        left+=nums[i]**2
    if left == nums[max_idx]**2:
        print("right")
    else:
        print("wrong")