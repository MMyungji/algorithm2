for tc in range(1,11):
    n = int(input())
    field = [list(map(int,input().split())) for _ in range(n)]
    cnt=0
    for col in range(n):
        idx=-1
        is_N = False
        while True:
            idx+=1
            if idx==n:
                break
            if field[idx][col]==1:
                is_N=True
            elif field[idx][col]==2:
                if is_N:
                    cnt+=1
                    is_N=False
    #
    # for j in range(n):
    #     stack = []
    #     is_N = False
    #     for i in range(n):
    #         if field[i][j]==1:
    #             stack.append(1)
    #             is_N=True
    #         if field[i][j]==2 and is_N:
    #             stack.clear()
    #             cnt+=1


    print(f"#{tc} {cnt}")