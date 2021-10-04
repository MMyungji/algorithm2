# 시간초과
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
print("\n".join(map(str,nums)))

# 정답
import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()
print("\n".join(map(str,nums)))


# Merge Sort Algorithm (병합 정렬) - O(N)
'''
def merge_sort(array):
    if len(array)<=1:
        return array
    
    # 재귀함수를 이용해서 끝까지 분할
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0

    # 분할된 배열끼리 비교
    while i<len(left) and j <len(right):
        if left[i]<right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k+=1
    
    # 먼저 끝났을 때 
    if i==len(left):
        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1
    elif j==len(right):
        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1
    return array
'''