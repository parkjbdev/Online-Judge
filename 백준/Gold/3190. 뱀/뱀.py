from collections import deque

N = int(input())
K = int(input())

BOARD = [[0 for _ in range(N)] for _ in range(N)]

for i in range(K):
    x, y = tuple(map(int, input().split()))
    BOARD[x - 1][y - 1] = -1

L = int(input())
MOVES = deque()

for i in range(L):
    X, C = input().split()
    MOVES.append((int(X), C))

time = 0
head = (0, 0)
BOARD[0][0] = 1
dxdys = [(0, 1), (1, 0), (0, -1), (-1, 0)]
diridx = 0

dq = deque()
dq.append((0, 0))

def in_range(next_head):
    x, y = next_head
    return 0 <= x < N and 0 <= y < N

while True:
    time += 1

    if not in_range((head[0] + dxdys[diridx][0], head[1] + dxdys[diridx][1])):
        break

    dx, dy = dxdys[diridx]

    # 사과가 있는경우.. 꼬리 그냥 두기
    # 없으면.. tail pop

    if BOARD[head[0] + dx][head[1] + dy] > 0:
        break
    if BOARD[head[0] + dx][head[1] + dy] != -1:
        tx, ty = dq.popleft()
        BOARD[tx][ty] = 0


    head = (head[0] + dx, head[1] + dy)
    BOARD[head[0]][head[1]] = 1
    dq.append(head)

    if MOVES and MOVES[0][0] == time:
        X, C = MOVES.popleft()
        if C == 'L': diridx += 3
        else: diridx += 1
        diridx %= 4

print(time)