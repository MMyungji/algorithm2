N = int(input())
ans = 0
cnt_5,cnt_3 = N//5,0            # 5의 배수부터 시작하기
# while True:
#     # print(cnt_3,cnt_5)
#     if cnt_5*5+cnt_3*3 == N:  # 값이 맞으면 출력
#         print(cnt_3+cnt_5)
#         break
#     if cnt_5*5+cnt_3*3>N:     # N보다 크면 -1출력
#         print(-1)
#         break
#     if (N-cnt_5*5)%3 != 0:    # 5 가방에 넣고 나머지가 3의 배수인지
#         if cnt_5 > 0:         # 3의 배수 아니면, 3 가방+=1 5가방-=1
#             cnt_5-=1
#         cnt_3+=1
#     else:                     #3의 배수이면 3 가방 더하기
#         cnt_3=(N-cnt_5*5)//3


while N>=0:
    if N%5 == 0: # 5의 배수이면 5로 나눈 몫 더하고 끝내기
        ans+=(N//5)
        print(ans)
        break
    N-=3        # 5의 배수가 아니면 3을 뺴주기
    ans+=1

