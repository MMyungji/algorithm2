def solve(k,n):
    data = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]+[[0]*15 for _ in range(14)]
    a,b=1,0
    while True:
        b += 1
        if b==15:
            a+=1
            b=1
        data[a][b] = sum(data[a-1][:b+1])
        # print(a,b,data[a][b])
        if a == k and b == n:
            break

    print(data[k][n])

tc = int(input())
for _ in range(tc):
    k = int(input())
    n = int(input())
    solve(k,n)
