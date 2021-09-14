nums = [int(input()) for _ in range(9)]

print(max(nums))
print(nums.index(max(nums))+1)


# max_num = max(nums)
# which = -1
# for i in range(len(nums)):
#     if max_num == nums[i]:
#         which = i+1
# print(max_num)
# print(which)
