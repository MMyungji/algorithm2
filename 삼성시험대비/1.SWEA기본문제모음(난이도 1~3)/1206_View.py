for tc in range(1,11):
    n = int(input())
    views = list(map(int,input().split()))
    cnt = 0

    for i in range(2,n-2):
        max_views = max(*views[i-2:i], *views[i+1:i+3])
        if max_views < views[i]:
            cnt+=views[i]-max_views

    print(f"#{tc} {cnt}")