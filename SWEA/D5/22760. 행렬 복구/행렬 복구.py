def find_first_row_idx(MAP):
    for i in range(len(MAP)):
        for j in range(i + 1, len(MAP)):
            if MAP[i][0] == MAP[j][0]:
                return i, j


def solution(MAP):
    ref_i, ref_j = find_first_row_idx(MAP)

    A = [None for i in range(len(MAP) // 2)]
    A[0] = MAP[ref_i]
    ref = MAP[ref_j]

    for idx in range(1, len(MAP) // 2):
        for i in range(len(MAP)):
            if MAP[i][0] == ref[idx]:
                A[idx] = MAP[i]

    return A


T = int(input())

for i in range(T):
    N = int(input())
    B = []
    for i in range(2 * N):
        B.append(list(map(int, input().split())))

    answer = solution(B)
    for e in answer:
        print(*e)