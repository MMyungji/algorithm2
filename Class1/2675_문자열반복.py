T = int(input())
for _ in range(T):
    R,S = input().split()
    res = ''
    for s in S:
        for _ in range(int(R)):
            res+=s
    print(res)