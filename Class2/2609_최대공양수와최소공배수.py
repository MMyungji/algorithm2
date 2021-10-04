n1,n2 = map(int,input().split())
# 유클리드 호제법
'''
x,y의 최대공약수는 y,r의 최대공약수와 같다
x%y == r
'''
def GCD(x,y):
    while y: #y가 참 = 자연수
        x,y=y,x%y
    return x

print(GCD(n1,n2))

def LCM(x,y):
    return (x*y)//GCD(x,y)

print(LCM(n1,n2))

# math 라이브러리
import math
print(math.gcd(n1,n2))
print(math.lcm(n1,n2))