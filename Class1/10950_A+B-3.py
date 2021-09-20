N = int(input())
nums = [list(map(int,input().split())) for _ in range(N)]
for n1,n2 in nums:
    print(n1+n2)