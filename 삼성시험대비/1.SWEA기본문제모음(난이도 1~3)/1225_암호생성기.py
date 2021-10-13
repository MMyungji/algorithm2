for _ in range(10):
    tc = int(input())
    pw = list(map(int,input().split()))
    cycle=0
    while True:
        cycle=(cycle)%5+1
        temp = pw.pop(0)-cycle
        if temp<=0:
            pw.append(0)
            break
        pw.append(temp)
    print(f"#{tc} {' '.join(map(str,pw))}")
