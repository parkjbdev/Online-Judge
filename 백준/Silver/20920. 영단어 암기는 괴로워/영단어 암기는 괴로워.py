from collections import defaultdict

N, M = map(int, input().split())

word_dict = defaultdict(int)

for i in range(N):
    word = input()
    if len(word) < M: continue
    word_dict[word] += 1

print(*list(map(lambda x: x[0], sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))), sep="\n")

