for _ in range(10):
    tc = int(input())
    data = [list(map(int,input().split())) for _ in range(100)]
    answer = 0
    data2 = list(map(list, zip(*data)))
    for i in range(100):
        answer = max(answer, sum(data[i]), sum(data2[i]))
    sum1=0
    sum2=0
    for i in range(100):
        sum1 += data[i][i]
        sum2 += data[i][99-i]
    answer = max(answer, sum1, sum2)

    print(f"#{tc} {answer}")
