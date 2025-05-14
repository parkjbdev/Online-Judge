N, K = map(int, input().split())
DABs = [tuple(map(int, input().split())) for _ in range(K)]

s = set()

for dab in DABs:
    x, y = dab

    if x - 2 >= 1:
        s.add((x - 2, y))
    if y - 2 >= 1:
        s.add((x,y - 2))
    if x + 2 <= N:
        s.add((x + 2, y))
    if y + 2 <= N:
        s.add((x,y + 2))

for dab in DABs:
    if dab in s:
        s.remove(dab)

print(len(s))

