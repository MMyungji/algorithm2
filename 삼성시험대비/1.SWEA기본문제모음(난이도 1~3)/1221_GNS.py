for _ in range(1,int(input())+1):
    tc, n = input().split()
    n = int(n)
    data = list(input().split())
    strs = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    nums = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
    sorting=[]
    answer = []
    for num in data:
        sorting.append(strs[num])
    sorting.sort()
    for num in sorting:
        answer.append(nums[num])
    print(f"{tc} {' '.join(answer)}")



    # for i in range(n):
    #     data[i]=strs[data[i]]
    # data.sort()
    # for i in range(n):
    #     data[i]=nums[data[i]]
    #
    # print(f"{tc} {' '.join(data)}")

