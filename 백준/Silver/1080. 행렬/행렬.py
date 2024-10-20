def solution(N, M, MATRIX):
    def flip_3by3(x, y):
        if not (0 <= x and x + 2 < N and 0 <= y and y + 2 < M):
            return False

        for i in range(3):
            for j in range(3):
                MATRIX[x + i][y + j] = not MATRIX[x + i][y + j]

        return True

    cnt = 0

    for i in range(N):
        for j in range(M):
            if MATRIX[i][j] == 1:
                if flip_3by3(i, j):
                    cnt += 1
                else:
                    return -1
    return cnt


N, M = map(int, input().split())
MATRIX = [list(map(int, list(input()))) for _ in range(N)]

for i in range(N):
    goal = list(map(int, list(input())))
    for j in range(M):
        MATRIX[i][j] = bool(MATRIX[i][j] ^ goal[j])

print(solution(N, M, MATRIX))
