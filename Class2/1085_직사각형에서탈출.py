x,y,w,h = map(int,input().split())
steps=[]
steps.extend([x,y,abs(x-w),abs(y-h)])
print(min(steps))