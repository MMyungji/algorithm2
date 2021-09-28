# 소수구하기 - 에리토스테네스의 체
N,M = map(int,input().split())
res = [False,False]+[True]*(M-1)
primes=[]
for i in range(2,M+1):
    if res[i]:
        if N<=i<=M:
            primes.append(i)
        for j in range(2*i,M+1,i):
            res[j] = False
print("\n".join(map(str,primes)))