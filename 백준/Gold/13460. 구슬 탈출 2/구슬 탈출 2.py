from collections import deque

N, M = map(int, input().split())
board = []
answer = 0

red = (0, 0)
blue = (0, 0)

for i in range(N):
    line = list(input())
    board.append(line)

    if 'R' in line:
        idx = line.index('R')
        red = (i, idx)
        board[i][idx] = '.'

    if 'B' in line:
        idx = line.index('B')
        blue = (i, idx)
        board[i][idx] = '.'

    if 'O' in line:
        idx = line.index('O')

# 목표: R구슬을 O로, B구슬은 절대 안빠지게

dxdy = [(1, 0), (-1, 0), (0, -1), (0, 1)]

visit = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
visit[red[0]][red[1]][blue[0]][blue[1]] = True

q = deque()
q.append((red, blue))

lq = deque()
lq.append(0)
l = 0

while q:
    (rx, ry), (bx, by) = q.popleft()
    l = lq.popleft()

    if l >= 10: continue

    for (dx, dy) in dxdy:
        nrx, nry = rx, ry
        nbx, nby = bx, by

        redExit = False
        blueExit = False

        mr = 0
        while board[nrx + dx][nry + dy] != '#':
            nrx += dx
            nry += dy
            mr += 1
            if board[nrx][nry] == 'O':
                redExit = True
                break

        mb = 0
        while board[nbx + dx][nby + dy] != '#':
            nbx += dx
            nby += dy
            mb += 1
            if board[nbx][nby] == 'O':
                blueExit = True
                break

        if blueExit: continue
        elif redExit:
            print(l + 1)
            exit(0)

        if (nrx, nry) == (nbx, nby):
            # blue가 더 갔음
            if mr < mb:
                nbx -= dx
                nby -= dy
            # red가 더 갔음
            else:
                nrx -= dx
                nry -= dy

        if visit[nrx][nry][nbx][nby]: continue

        visit[nrx][nry][nbx][nby] = True
        q.append(((nrx, nry), (nbx, nby)))
        lq.append(l + 1)

print(-1)
