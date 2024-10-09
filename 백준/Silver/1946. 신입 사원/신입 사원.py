def solution():
    N = int(input())
    SCORES = sorted(
        [tuple(map(int, input().split())) for _ in range(N)],
        key=lambda x: (x[0], x[1]),
    )

    best_score = SCORES[0][1]

    cnt = 0
    for _, score in SCORES:
        if best_score < score:
            continue
        cnt += 1
        best_score = score

    return cnt


T = int(input())
print(*[solution() for _ in range(T)], sep="\n")
