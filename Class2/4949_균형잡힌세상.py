# 모든 예외상황 고려하기
while True:
    data = input()
    if data==".":
        break
    stack,flag = [],True
    for word in data:
        if word == "(" or word == "[":
            stack.append(word)
        elif word == ")":
            if stack:
                temp = stack.pop()
                if temp != "(":
                    flag = False
                    break
            else:
                flag = False
                break
        elif word == "]":
            if stack:
                temp = stack.pop()
                if temp != "[":
                    flag = False
                    break
            else:
                flag = False
                break
    if stack or flag==False:
        print("no")
    else:
        print("yes")