from collections import deque

N, M = map(int, input().split())
MAP = [input() for _ in range(N)]

START = (0, 0)
for i in range(N):
    for j in range(M):
        if MAP[i][j] == '0':
            START = (i, j)


x = START[0]
y = START[1]


def bfs():
    global x, y

    VISITED = [[[False for _ in range(0b1000000)]
                for _ in range(M)] for _ in range(N)]

    VISITED[x][y][0] = True

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    queue = deque([(x, y, 0, 0)])

    while queue:
        x, y, keys, level = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if VISITED[nx][ny][keys] or MAP[nx][ny] == '#':
                continue
            elif MAP[nx][ny] == '1':
                x, y = nx, ny
                return level + 1
            elif MAP[nx][ny] in ['.', '0']:
                if not VISITED[nx][ny][keys]:
                    VISITED[nx][ny][keys] = True
                    queue.append((nx, ny, keys, level + 1))
            elif MAP[nx][ny].isupper():
                if keys & (1 << (ord(MAP[nx][ny].lower()) - ord('a'))) != 0:
                    if not VISITED[nx][ny][keys]:
                        VISITED[nx][ny][keys] = True
                        queue.append((nx, ny, keys, level + 1))
            elif MAP[nx][ny].islower():
                tmp_keys = keys | (1 << (ord(MAP[nx][ny]) - ord('a')))
                if not VISITED[nx][ny][tmp_keys]:
                    VISITED[nx][ny][tmp_keys] = True
                    queue.append((nx, ny, tmp_keys, level + 1))

    return -1


answer = bfs()
print(answer)
