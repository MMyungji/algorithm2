# 브루트포스
N = int(input())
res = 666
cnt=0
while True:
    if '666' in str(res):
        cnt+=1
    if cnt == N:
        print(res)
        break
    res+=1