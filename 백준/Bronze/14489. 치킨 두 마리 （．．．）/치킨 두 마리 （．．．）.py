A, B = map(int, input().split())
C = int(input())

print(A + B if (A + B) < C * 2 else A + B - C * 2)
