def solution(n,m):
    if m==1:
        return n
    return n*solution(n,m-1)

for _ in range(10):
    n = int(input())
    a,b=map(int,input().split())
    # print(f"#{n} {a**b}")
    print(f"#{n} {solution(a,b)}")