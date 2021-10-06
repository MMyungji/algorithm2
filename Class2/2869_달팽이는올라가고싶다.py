# 시간초과
# import sys
# input = sys.stdin.readline
# A,B,V = map(int,input().split())
# days,now=0,0
# while True:
#     days+=1
#     now+=A
#     if now>=V:
#         print(days)
#         break
#     now-=B


A,B,V = map(int,input().split())
days=0
# 달팽이는 하루에 A-B 만큼 이동
# 마지막 V-B만큼 가게됨 (목표지점에서는 미끄러지지 않음)
if (V-B)%(A-B)!=0:
    days = (V-B)//(A-B)+1
else:
    days = (V-B)//(A-B)
print(days)