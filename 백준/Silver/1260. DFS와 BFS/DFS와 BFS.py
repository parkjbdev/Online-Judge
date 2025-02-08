N, M, V = map(int, input().split())
V -= 1
EDGES = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    EDGES[a].append(b)
    EDGES[b].append(a)
    EDGES[a].sort()
    EDGES[b].sort()

def dfs():
    visited = [False for _ in range(N)]
    def _dfs(v, visited):
        visited[v] = True
        print(v + 1, end=' ')
        for edge in EDGES[v]:
            if not visited[edge]:
                _dfs(edge, visited)
    _dfs(V, visited)
    print()


def bfs():
    visited = [False for _ in range(N)]
    visited[V] = True

    def _bfs(start, visited):
        from collections import deque

        queue = deque([start])
        while queue:
            v = queue.popleft()
            print(v + 1, end=' ')
            for edge in EDGES[v]:
                if not visited[edge]:
                    queue.append(edge)
                    visited[edge] = True

    _bfs(V, visited)
    print()

dfs()
bfs()
