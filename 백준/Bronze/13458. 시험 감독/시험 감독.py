from math import ceil

N = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())

print(sum(list(map(lambda x: 1 + max(0, ceil((x - B) / C)), Ai))))