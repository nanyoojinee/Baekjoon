from collections import deque
n,m = map(int,input().split())
ab_list=[]
node_list = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  ab_list.append([a,b])


for a,b in ab_list:
  node_list[a].append(b)
  node_list[b].append(a)



def bfs(start):
    visited = [-1] * (n + 1)  # 방문하지 않은 노드는 -1로 초기화
    visited[start] = 0  # 시작 노드의 거리는 0
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in node_list[v]:
            if visited[i] == -1:  # 방문하지 않은 노드에 대해
                visited[i] = visited[v] + 1
                queue.append(i)
    return sum(filter(lambda x: x >= 0, visited))  # -1을 제외한 모든 거리의 합을 반환

result = float('inf')
min_kevin_man = -1

for i in range(1, n+1):
    kevin = bfs(i)
    if kevin < result:
        result = kevin
        min_kevin_man = i

print(min_kevin_man)