# 입력에서 초과시간이 생길때는 sys.stdin.readline() 사용하기

#통계 라이브러리 사용하기
'''
from statistics import*
n,*l=map(int,open(0))
print('%.0f'%mean(l),median(l),sorted(multimode(l))[:2][-1],max(l)-min(l))
'''

# N=int(input())
# nums = [int(input()) for _ in range(N)]
import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

print(round(sum(nums)/N))
print(nums[N//2])

mode_dict = dict(zip(nums, [0] * len(nums)))
for n in nums:
    mode_dict[n] += 1
modes = [k for k, v in mode_dict.items() if v == max(mode_dict.values())]
if len(modes)>1:
    print(modes[1])
else:
    print(modes[0])

print(max(nums)-min(nums))