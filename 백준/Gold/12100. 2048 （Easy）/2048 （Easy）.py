from collections import deque

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

def move(dx, dy, MAP):
    TMP_MAP = [row[:] for row in MAP]
    if (dx, dy) == (0, 1):
        # 좌우반전
        TMP_MAP = [row[::-1] for row in TMP_MAP]
    elif (dx, dy) == (-1, 0):
        # 반시계 90도
        TMP_MAP = list(map(list, zip(*TMP_MAP[::-1])))
    elif (dx, dy) == (1, 0):
        # 시계 90도
        TMP_MAP = list(map(list, zip(*TMP_MAP)))[::-1]

    for i in range(N):
        tmp = deque([x for x in TMP_MAP[i] if x != 0])
        res = []
        while tmp:
            n = tmp.popleft()
            if tmp and n == tmp[0]:
                tmp.popleft()
                res.append(n * 2)
            else:
                res.append(n)

        TMP_MAP[i] = res + [0] * (N - len(res))

    # 원상복구
    if (dx, dy) == (0, 1):
        # 좌우반전
        TMP_MAP = [row[::-1] for row in TMP_MAP]
    elif (dx, dy) == (-1, 0):
        # 시계 90도
        TMP_MAP = list(map(list, zip(*TMP_MAP)))[::-1]
    elif (dx, dy) == (1, 0):
        # 반시계 90도
        TMP_MAP = list(map(list, zip(*TMP_MAP[::-1])))

    return TMP_MAP


def move_i(i, MAP):
    if i == 0:
        return move(-1, 0, MAP)
    elif i == 1:
        return move(1, 0, MAP)
    elif i == 2:
        return move(0, -1, MAP)
    elif i == 3:
        return move(0, 1, MAP)

    return MAP

answer = 0

def dfs(board, depth=0):
    global answer
    if depth == 5:
        answer = max(answer, max(max(r) for r in board))
        return

    for direction in range(4):
        NMAP = move_i(direction, board)
        dfs(NMAP, depth + 1)

dfs(MAP)

print(answer)