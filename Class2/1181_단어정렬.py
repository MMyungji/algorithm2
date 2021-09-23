N = int(input())
words = set([input() for _ in range(N)])
res = list(words)
res.sort()
res.sort(key=len) #문자열 길이로 정렬
for word in res: print(word)


'''
# 시간초과
N = int(input())
words = sorted([input() for _ in range(N)])
res = []
for word in words:
    n = len(word)
    if [n,word] in res:
        continue
    res.append([n,word])
res = sorted(res, key=lambda x:x[0]) #1번째 요소를 기준으로 정렬하기
for i in range(len(res)):
    print(res[i][1])
'''
