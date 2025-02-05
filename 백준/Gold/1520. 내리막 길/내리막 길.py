import sys
sys.setrecursionlimit(100000)

# Input
M, N = map(int, input().split())

MAP = [[] for _ in range(M)]

for i in range(M):
    MAP[i] = list(map(int, input().split()))


memo = [[-1 for _ in range(N)] for _ in range(M)]
memo[M - 1][N - 1] = 1


def dfs(x, y):
    if memo[x][y] >= 0:
        return memo[x][y]
    else:
        memo[x][y] = 0

    result = 0

    if 0 <= x - 1 < M and 0 <= y < N and MAP[x - 1][y] < MAP[x][y]:
        result += dfs(x - 1, y)

    if 0 <= x < M and 0 <= y + 1 < N and MAP[x][y + 1] < MAP[x][y]:
        result += dfs(x, y + 1)

    if 0 <= x + 1 < M and 0 <= y < N and MAP[x + 1][y] < MAP[x][y]:
        result += dfs(x + 1, y)

    if 0 <= x < M and 0 <= y - 1 < N and MAP[x][y - 1] < MAP[x][y]:
        result += dfs(x, y - 1)

    memo[x][y] = result

    return result


print(dfs(0, 0))
