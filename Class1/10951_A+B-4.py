import sys

# 입력끝까지 받아오기 sys.stdin.readlines()
lines = sys.stdin.readlines()
# print(lines)
for line in lines:
    A,B = map(int,line.split())
    # print(A,B)
    print(A+B)
