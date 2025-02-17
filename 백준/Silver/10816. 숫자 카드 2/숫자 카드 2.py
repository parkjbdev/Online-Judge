from collections import defaultdict

hashmap = defaultdict(lambda: 0)
N = int(input())
Ns = list(map(int, input().split()))
for n in Ns:
    hashmap[n] += 1
M = int(input())
Ms = list(map(int, input().split()))
for m in Ms:
    print(hashmap[m], end=" ")
