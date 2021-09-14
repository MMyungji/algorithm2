def cycle(num):
    global count
    count+=1
    first = num%10
    if num<10:
        second = num
    else:
        temp = num%10
        num//=10
        temp += num%10
        second = temp%10
    # print(2,second)
    now = (first)*10+second
    # print('now:',now)
    if now == N:
        return count
    cycle(now)
N = int(input())
count = 0
cycle(N)
print(count)