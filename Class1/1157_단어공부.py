word = input()
count = {}
for w in word:
    if w.upper() in count:
        count[w.upper()]+=1
    else:
        count[w.upper()]=1
# print(list(count.values()))
max_num = max(list(count.values()))

res = []
for c,n in count.items():
    if n == max_num:
        res.append(c)
if len(res)>1:
    print('?')
else:
    print(res[0])

