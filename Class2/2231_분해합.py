#완탐

N = int(input())
res = 0
for i in range(1,N):
    nums = map(int,str(i))
    sum_nums = i+sum(nums)
    if sum_nums==N:
        print(i)
        res = i
        break
if res==0:
    print(0)

