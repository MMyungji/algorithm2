def is_ok(mat):
    for i in range(n//2):
        if mat[i]!=mat[-(i+1)]:
            break
    else:
        return True
    return False


for tc in range(1,11):
    n = int(input())
    data = [list(input()) for _ in range(8)]
    data2 = list(map(list,zip(*data)))
    cnt=0
    for i in range(8):
        for j in range(8):
            if j+n<=8:
                # print(data[i][j:j+n],is_ok(data[i][j:j+n]))
                if is_ok(data[i][j:j+n]):
                    cnt+=1
                # print(data2[i][j:j + n], is_ok(data2[i][j:j + n]))
                if is_ok(data2[i][j:j + n]):
                    cnt += 1

    print(f"#{tc} {cnt}")
