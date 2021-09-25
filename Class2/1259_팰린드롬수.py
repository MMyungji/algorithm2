while True:
    data = input()
    if data=="0":
        break
    res = "yes"
    # print(data[::-1])  #문자열 반대로 출력
    # print(data)
    for i in range(len(data)//2):  # if data[::-1]==num: res="yes"
        # print(data[i],data[-(i+1)])
        if data[i] != data[-(i+1)]:
            res = "no"
            break
    print(res)