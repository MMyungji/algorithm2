for tc in range(1,int(input())+1):
    # memory = list(map(int,input()))
    # N = len(memory)
    # now = [0]*N
    # cnt = 0
    # for i in range(N):
    #     if now == memory:
    #         break
    #     if now[i]==memory[i]:
    #        continue
    #     cnt+=1
    #     if now[i] == 1:
    #         c = 0
    #     else:
    #         c=1
    #     for j in range(i,N):
    #         now[j]=c

    memory = input()
    now=["0"]*len(memory)
    cnt=0
    for i in range(len(memory)):
        if now[i]!=memory[i]:
            now[i:]=memory[i]*len(now[i:])
            cnt+=1
    print(f"#{tc} {cnt}")
