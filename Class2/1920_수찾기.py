N = int(input())
data = set(map(int,input().split())) # 자료형 list보다 set이 빠름, set과 딕셔너리의 in연산 포함 여부 확인의 시간복잡도 O(1)
M = int(input())
inputs = list(map(int,input().split()))
for i in inputs:
    if i in data:
        print(1)
    else:
        print(0)