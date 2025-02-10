from itertools import combinations
from collections import deque
from math import inf

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

def bfs(active_viruses):
    DXs = [-1, 1, 0, 0]
    DYs = [0, 0, -1, 1]

    queue = deque(list(map(lambda x: (x[0], x[1], int(0)), active_viruses)))

    visit = [[False for _ in range(N)] for _ in range(N)]

    for x, y in active_viruses:
        visit[x][y] = True

    lastlevel = 0

    while queue:
        x, y, level = queue.popleft()

        shouldCount = True

        if MAP[x][y] == 2:
            shouldCount = False
            for dx, dy in zip(DXs, DYs):
                nx, ny = x + dx, y + dy
                if ( not (0 <= nx < N and 0 <= ny < N) ) or (visit[nx][ny] or MAP[nx][ny] != 0):
                    continue
                shouldCount = True
                break

        if shouldCount:
            lastlevel = max(lastlevel, level)

        for dx, dy in zip(DXs, DYs):
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visit[nx][ny] or MAP[nx][ny] == 1:
                continue

            elif MAP[nx][ny] != 1:
                visit[nx][ny] = True
                queue.append((nx, ny, level + 1))

    for i in range(N):
        for j in range(N):
            if not visit[i][j] and MAP[i][j] != 1:
                return -1

    return lastlevel

VIRUSES = []

flag = False
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 0:
            flag = True
if not flag:
    print(0)
    exit()

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 2:
            VIRUSES.append((i, j))

minlev = inf
for comb in combinations(VIRUSES, M):
    ret = bfs(list(comb))
    if ret != -1:
        minlev = min(minlev, ret)

if minlev == inf:
    print(-1)
else:
    print(minlev)