import math

n = int(input())

for i in range(n):
  raw = input().split()
  x, y = int(raw[0]), int(raw[1])
  print(math.comb(y, x))