N, C = map(int, input().split())
MAP = [int(input()) for _ in range(N)]
MAP.sort()

def possible(dist) :
    cnt = 1
    ptr = MAP[0]

    for i in range(1, N):
        if MAP[i] - ptr >= dist:
            ptr = MAP[i]
            cnt+=1

    return cnt >= C


target = 1

min_dist = 1
max_dist = MAP[N - 1] - MAP[0]

answer = 0

while min_dist <= max_dist:
    mid_dist = (min_dist + max_dist) // 2
    if possible(mid_dist):
        answer = max(answer, mid_dist)
        min_dist = mid_dist + 1
    else:
        max_dist = mid_dist - 1

print(answer)
