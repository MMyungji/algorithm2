N = int(input())
answer = 0
for i in range(N, 1000001):
    if i == 1: continue
    if i == 2:
        answer = i
        break
    if str(i) == str(i)[::-1]: # [::-1] 글자나 배열 '역순' 출력
        if i%2 == 0:
            continue
        flag = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                flag = False
                break
        if flag:
            answer = i
            break
if answer==0:
    answer = 1003001
print(answer)