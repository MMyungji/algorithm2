# 이분탐색 (조건: 랜선의 길이는 2**31-1보다 작거나 같은 자연수)
K,N = map(int,input().split())
lines = [int(input()) for _ in range(K)]
start, end = 1, max(lines)
while start<=end:
    mid = (start+end)//2
    cnt=0
    for line in lines:
        cnt += line//mid
    if cnt>=N:
        start = mid+1
    else:
        end = mid-1
# print(start)
print(end)