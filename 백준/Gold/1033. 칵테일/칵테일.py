from collections import deque
N = int(input())
ANSWER = [0 for _ in range(N)]
INPUT = [tuple(map(int, input().split())) for _ in range(N - 1)]
queue = deque()
todos = []


def calc_gcd(a, b):
    return a if b == 0 else calc_gcd(b, a % b)


def calc_lcm(a, b):
    gcd = calc_gcd(a, b)
    return (a // gcd) * (b // gcd) * gcd

queue.extend(INPUT)

cnt = 0

while queue:
    a, b, p, q = queue.popleft()
    gcd = calc_gcd(p, q)
    p //= gcd
    q //= gcd

    if cnt == 0:
        ANSWER[a] = p
        ANSWER[b] = q
    cnt += 1

    if ANSWER[a] == 0 and ANSWER[b] == 0:
        queue.append((a, b, p, q))
        continue

    if ANSWER[a] == 0 and ANSWER[b] != 0:
        a, b = b, a
        p, q = q, p
    
    lcm = calc_lcm(ANSWER[a], p)
    diff = lcm // ANSWER[a]
    ANSWER = list(map(lambda x: x * diff, ANSWER))
    ANSWER[a] = lcm
    ANSWER[b] = q * (lcm // p)

print(*ANSWER)
