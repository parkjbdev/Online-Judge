from collections import deque
from collections import defaultdict

N, K = map(int, input().split())


def bfs(N, K):
    BOUND = 100001
    queue = deque([(N, 0)])

    visited = defaultdict(lambda: False)
    visited[N] = True

    while queue:
        x, level = queue.popleft()

        if x == K:
            return level

        if 0 <= x - 1 < BOUND and not visited[x - 1]:
            visited[x - 1] = True
            queue.append((x - 1, level + 1))
        if 0 <= x + 1 < BOUND and not visited[x + 1]:
            visited[x + 1] = True
            queue.append((x + 1, level + 1))
        if 0 <= 2 * x < BOUND and not visited[2 * x]:
            visited[2 * x] = True
            queue.append((2 * x, level + 1))


print(bfs(N, K))