for _ in range(int(input())):
    data = list(input())
    level,max_level = 0,0
    for i in range(len(data)):
        if data[i] == "[":
            level+=1
            if level>max_level: max_level=level
        else:
            level-=1
    print(2**max_level)
