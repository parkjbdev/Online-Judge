BOARD = [list(map(int, input().split())) for _ in range(9)]
BLANKs = []

Xs = [0] * 9
Ys = [0] * 9
Zs = [0] * 9


def group_z(x, y):
    return (x // 3) * 3 + y // 3


for i in range(9):
    for j in range(9):
        if BOARD[i][j] == 0:
            BLANKs.append((i, j))
        else:
            Xs[i] |= (1 << BOARD[i][j])
            Ys[j] |= (1 << BOARD[i][j])
            Zs[group_z(i, j)] |= (1 << BOARD[i][j])


def get_candidates(x, y):
    cand1 = Xs[x]
    cand2 = Ys[y]
    cand3 = Zs[group_z(x, y)]
    cands = set()
    cand_bit = cand1 | cand2 | cand3

    for i in range(1, 10):
        if (cand_bit >> i) & 0b1 == 0b0:
            cands.add(i)
    return cands


def mark_at(x, y, n):
    global BOARD, Xs, Ys, Zs
    Xs[x] |= (1 << n)
    Ys[y] |= (1 << n)
    Zs[group_z(x, y)] |= (1 << n)
    BOARD[x][y] = n


def unmark_at(x, y, n):
    global BOARD, Xs, Ys, Zs
    Xs[x] &= ~(1 << n)
    Ys[y] &= ~(1 << n)
    Zs[group_z(x, y)] &= ~(1 << n)
    BOARD[x][y] = 0


def backtracking():
    if len(BLANKs) == 0: return True

    BLANKs.sort(key=lambda k: len(get_candidates(*k)))
    x, y = BLANKs[0]

    cands = get_candidates(x, y)

    for cand in cands:
        mark_at(x, y, cand)
        BLANKs.remove((x, y))
        if backtracking(): return True
        BLANKs.append((x, y))
        unmark_at(x, y, cand)

    return False


backtracking()
for i in range(9):
    print(*BOARD[i])
