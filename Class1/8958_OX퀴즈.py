for _ in range(int(input())):
    scores=input()
    prev=''
    count=0
    res=0
    for score in scores:
        if score=='O':
            if prev=='' or prev=='O':
                count+=1
            else:
                count=0
            res+=count
        else:
            count=0
            res+=count
    print(res)