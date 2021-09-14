def all_same_color(cards):
    if len(cards)==1:
        return True
    return False

def isContinue(num_cnt):
    #print(num_cnt)
    idx = 0
    for n in range(1,10):
        if num_cnt[n] > 1: return False
        if num_cnt[n] == 1:
            idx = n
            break
    # print("idx",idx)
    if idx == 0: return False
    for n in range(idx,idx+5):
        if num_cnt[n] != 1:
            return False
    return True

cards = {}
num_cnt = [0 for _ in range(10)]
nums = set()
answer = 0
for _ in range(5):
    c, n = input().split()
    n = int(n)
    if c in cards:
        cards[c].append(n)
    else:
        cards[c] = [n]
    num_cnt[n]+=1
    nums.add(n)

counts = sorted(num_cnt,reverse=True)
nums = list(nums)
#print(all_same_color(cards))
#print(isContinue(num_cnt))


if all_same_color(cards):
    if isContinue(num_cnt):
        answer = max(answer, 900+max(nums))
    else:
        answer = max(answer, 600+max(nums))
if isContinue(num_cnt):
    answer = max(answer, 500+max(nums))
if counts[0]==4:
    num = num_cnt.index(4)
    answer = max(answer, 800+num)
if counts[0]==3:
    n1 = num_cnt.index(3)
    if counts[1]==2:
        n2 = num_cnt.index(2)
        answer = max(answer, n1*10+n2+700)
    else:
        answer = max(answer, n1+400)
if counts[0]==2:
    num = []
    for i in range(10):
        if num_cnt[i]==2:
            num.append(i)
    if len(num)==2:
        num = sorted(num, reverse=True)
        answer = max(answer, num[0]*10+num[1]+300)
    else:
        answer = max(answer, num[0]+200)
answer = max(answer, max(nums)+100)

print(answer)

