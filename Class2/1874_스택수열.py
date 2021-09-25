N = int(input())
order = [int(input()) for _ in range(N)]
stack=[]
res = []
current=1
for target in order:
    while current<=target:
        res.append("+")
        stack.append(current)
        current+=1
    if stack[-1] == target:
        stack.pop()
        res.append("-")
if stack:
    print("NO")
else:
    print("\n".join(res))
