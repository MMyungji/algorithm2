# 트리를 그래프로 구현 -> 부모노드 찾기(dfs,bfs)
# 그래프처럼 순회하지 않고 한방향으로만 내려가므로 visited 리스트 필요없음
import sys
input = sys.stdin.readline

N = int(input())
graph_tree = [[] for _ in range(N+1)]
parents = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    graph_tree[a].append(b)
    graph_tree[b].append(a)

stack = [1]
while stack:
    node = stack.pop()
    for i in graph_tree[node]:
        stack.append(i)
        graph_tree[i].remove(node)
        parents[i].append(node)

for i in range(2,N+1):
    print(parents[i][0])


# 런타임에러
# N = int(input())
# dic = {1:0}
# for _ in range(N-1):
#     a,b = map(int,input().split())
#     if a in dic:
#         dic[b]=a
#     else:
#         dic[a]=b
# for i in range(2,N+1):
#     print(dic[i])