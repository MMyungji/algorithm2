n = int(input())
scores = list(map(int,input().split()))
max_score = max(scores)
after = [s/max_score*100 for s in scores]
print(sum(after)/n)