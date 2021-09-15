H,M = map(int,input().split())
if M-45<0:
    if H-1<0:
        H=H-1+24
    else:
        H-=1
    M=M-45+60
else:
    M=M-45
print(H,M)