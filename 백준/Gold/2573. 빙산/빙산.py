DXDY = [(-1, 0), (0, 1), (1, 0), (0, -1)]
M, N = map(int, input().split())
BOARD = [list(map(int, input().split())) for _ in range(M)]
COORDs = set()

for i in range(M):
    for j in range(N):
        if BOARD[i][j] != 0:
            COORDs.add((i, j))



def add_to_board(to_add):
    global BOARD

    for x, y, adder in to_add:
        if BOARD[x][y] + adder <= 0:
            BOARD[x][y] = 0
            COORDs.remove((x, y))
        else: BOARD[x][y] += adder

def age():
    to_add = []

    for x, y in COORDs:
        cnt = 0
        for dx, dy in DXDY:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < M and 0 <= ny < N): continue
            if BOARD[nx][ny] == 0: cnt += 1

        to_add.append((x, y, -cnt))

    add_to_board(to_add)

def count_groups_bfs():
    from collections import deque

    cnt = 0

    visit = [[False for _ in range(N)] for _ in range(M)]

    for sx, sy in COORDs:
        if visit[sx][sy]: continue

        cnt += 1

        q = deque([(sx, sy)])
        visit[sx][sy] = True

        while q:
            x, y = q.popleft()
            for dx, dy in DXDY:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < M and 0 <= ny < N): continue
                if visit[nx][ny]: continue
                if BOARD[nx][ny] == 0: continue

                visit[nx][ny] = True
                q.append((nx, ny))

    return cnt

year = 0
while COORDs:
    age()
    year += 1
    if count_groups_bfs() >= 2: break
else:
    print(0)
    exit(0)

print(year)