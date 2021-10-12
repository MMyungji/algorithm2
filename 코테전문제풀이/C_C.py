# monster = [(-2,-2), (2,-2), (2,2)]  #몬스터위치
# hunter = (0,0)                      #사냥꾼 시작 위치(x,y)
# r = 1                               #사정거리: 사냥꾼의 위치(x,y)에서 몬스터의 위치의 차가 x,y모두 r이하

monster = [(1,1),(0,0),(2,0),(2,2),(0,2)]
hunter=(1,1)
r=0

dir = [(-1,0),(0,-1),(1,0),(0,1)]
answer = -1
catched = set()
is_catched = False
d=-1
while True:
    if catched == set(monster):
        break
    answer+=1
    if not is_catched:
        d=(d+1)%4
    now_catched=False
    for mx,my in monster:
        if hunter[0]-r <= mx <= hunter[0]+r and hunter[1]-r <= my <= hunter[1]+r:
            catched.add((mx,my))
            is_catched = True
            now_catched=True
    if not now_catched:
        is_catched=False

    hunter = (hunter[0]+dir[d][0],hunter[1]+dir[d][1])
print(answer)


