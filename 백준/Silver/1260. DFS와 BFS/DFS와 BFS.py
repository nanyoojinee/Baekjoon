from collections import deque

# 그래프 입력 받기
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 탐색하기 쉽게 각 노드에 연결된 노드들을 정렬
for connection in graph:
    connection.sort()

# DFS 구현
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 구현
def bfs(graph, start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 방문 여부 확인을 위한 리스트
visited = [False] * (N + 1)

# DFS와 BFS 실행
dfs(graph, V, visited)
print()  # 줄바꿈
bfs(graph, V)
