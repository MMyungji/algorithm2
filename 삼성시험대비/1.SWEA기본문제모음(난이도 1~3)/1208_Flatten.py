'''
for test_case in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        box[box.index(max(box))] -= 1   #max의 인덱스를 찾아 -1
        box[box.index(min(box))] += 1   #min의 인덱스를 찾아 +1

    print('#' + str(test_case), max(box) - min(box))
'''

def solution(data):
    max_num, min_num = 0, 987654321
    max_idx, min_idx = -1,-1
    for i in range(100):
        if data[i]<min_num:
            min_num=data[i]
            min_idx = i
        if data[i]>max_num:
            max_num=data[i]
            max_idx = i
    data[max_idx]-=1
    data[min_idx]+=1
    return data

for tc in range(1,11):
# for tc in range(1):
    n = int(input())
    data = list(map(int,input().split()))

    for _ in range(n):
        data= solution(data)
        # print(max(data),min(data))
        ans = max(data) - min(data)
        if ans == 1 or ans == 0:
            break
    print(f"#{tc} {ans}")