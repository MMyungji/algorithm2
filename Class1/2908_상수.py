A,B = input().split()
a,b=0,0
for i in range(3):
    a+=int(A[i])*10**i
    b+=int(B[i])*10**i
if a>b:
    print(a)
else:
    print(b)