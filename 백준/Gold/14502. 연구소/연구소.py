from collections import deque
from itertools import combinations

DXDY = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(N)]

viruses = []
empties = []

for i in range(N):
    for j in range(M):
        if BOARD[i][j] == 2:
            viruses.append((i, j))
        elif BOARD[i][j] == 0:
            empties.append((i, j))

answer = 0

visit = [[0 for _ in range(M)] for _ in range(N)]
vtag = 0

def bfs(BOARD, viruses, vtag):
    q = deque(viruses)

    for x, y in viruses:
        visit[x][y] = vtag

    clean = len(empties)

    while q:
        vx, vy = q.popleft()

        for dx, dy in DXDY:
            nx = vx + dx
            ny = vy + dy

            if not (0 <= nx < N and 0 <= ny < M): continue
            if visit[nx][ny] == vtag: continue
            if BOARD[nx][ny] == 1: continue

            clean -= 1
            if answer > clean - 3: return clean - 3

            visit[nx][ny] = vtag
            q.append((nx, ny))

    return clean - 3

combs = combinations(empties, 3)
for walls in combs:
    for x, y in walls:
        BOARD[x][y] = 1

    vtag += 1

    answer = max(answer, bfs(BOARD, viruses, vtag))

    for x, y in walls:
        BOARD[x][y] = 0

print(answer)