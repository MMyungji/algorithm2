def dfs(queen, row, n):
    count = 0
    # (체스판 8 * 8 기준) 마지막 줄까지 퀸을 놓은 경우(총 8개 놓음) 가능한 경우이므로 true(1) 리턴
    if n == row:
        print(f"queen: {queen}")
        return 1

    for col in range(n):
        queen[row] = col  # 우선 현재의 row행에 col 값을 넣어준다.
        for i in range(row):
            # 만약 조금전에 넣은 row행의 col 값이 이전의 행에 넣은 col 값과 겹치는 경우
            # 백트래킹 처리(뒤로 가준다) 해준다.
            if queen[i] == queen[row]:
                break
            # line 15의 조건은 대각선 방향으로 겹치는게 있는지 확인하는 코드
            if abs(queen[i] - queen[row]) == row - i:
                break
        # 만약 이때까지 놓은 모든 퀸이 col(열)이 겹치지 않고 대각선도 하나도 안겹친다면
        # 다음위치로 이동한다.
        else:
            count += dfs(queen, row + 1, n)
    print(f"q: {queen}, c: {count}")
    return count


def solution(n):
    return dfs([0] * n, 0, n)

print(solution(4))