N = int(input())

def nqueen(N, row, cols, diags_left, diags_right):
    if row == N:
        return 1

    cnt = 0
    for i in range(N):
        if cols[i] or diags_left[i + row] or diags_right[N - 1 - row + i]:
            continue
        cols[i] = diags_left[i + row] = diags_right[N - 1 - row + i] = True
        cnt += nqueen(N, row + 1, cols, diags_left, diags_right)
        cols[i] = diags_left[i + row] = diags_right[N - 1 - row + i] = False

    return cnt

print(nqueen(N, 0, [False] * N, [False] * (2 * N - 1), [False] * (2 * N - 1)))
