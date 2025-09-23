N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))

# dice = [
#     [0, 2, 0],
#     [4, 1, 3],
#     [0, 5, 0],
#     [0, 6, 0]
# ]

dice = [
    [0 for _ in range(3)] for _ in range(4)
]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


for cmd in direction:
    if cmd == 1:  # 동
        if not in_range(x, y + 1):
            continue
        else:
            y += 1
            dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    elif cmd == 2:  # 서
        if not in_range(x, y - 1):
            continue
        else:
            y -= 1
            dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    elif cmd == 3:  # 북
        if not in_range(x - 1, y):
            continue
        else:
            x -= 1
            dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    elif cmd == 4:  # 남
        if not in_range(x + 1, y):
            continue
        else:
            x += 1
            dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]

    if board[x][y] == 0:
        board[x][y] = dice[3][1]
    else:
        dice[3][1] = board[x][y]
        board[x][y] = 0


    print(dice[1][1])