for tc in range(int(input())):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]
    harvest = 0
    # 방법 1
    # start = N//2
    # for i in range(N//2):
    #     idx=2*i+1
    #     # print(i,start,idx)
    #     harvest += sum(farm[i][start:start+idx])
    #     start-=1
    # start=N//2
    # for i in range(N-1,N//2-1,-1):
    #     idx=2*(N-1-i)+1
    #     # print(i, start, idx)
    #     harvest+=sum(farm[i][start:start+idx])
    #     start-=1

    # 방법 2
    mid = N//2
    start,end = mid,mid
    for i in range(N):
        harvest += sum(farm[i][start:end+1])
        if i < mid:
            start,end = start-1,end+1
        else:
            start,end = start+1,end-1

    print(f"#{tc+1} {harvest}")
