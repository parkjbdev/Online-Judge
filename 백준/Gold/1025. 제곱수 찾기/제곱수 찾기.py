def solution(N, M, A):
    answer = -1

    def is_squarenum(n):
        import math

        k = math.floor(n**0.5)
        return k**2 == n

    for rowd in range(-N, N):
        for cold in range(-M, M):
            if rowd == 0 and cold == 0:
                continue
            for i in range(N):
                for j in range(M):
                    x, y = i, j
                    number = 0
                    while 0 <= x < N and 0 <= y < M:
                        number *= 10
                        number += int(A[x][y])
                        if is_squarenum(number):
                            answer = max(answer, number)
                        x += rowd
                        y += cold

    return answer


N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]

print(solution(N, M, A))
