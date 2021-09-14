num, who = map(int,input().split())
medals = [list(map(int,input().split())) for _ in range(num)]
medals.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)
grade=0
scores = [medals[0][1], medals[0][2], medals[0][3]]
same_grade=0
#print(medals)
for n,g,s,b in medals:
    #print(scores, grade, same_grade)
    if scores == [g,s,b]:
        same_grade+=1
    else:
        grade+=1+same_grade
        same_grade = 0
        scores = [g,s,b]
    if n == who:
        if grade==0:
            grade=1
        print(grade)
        break
