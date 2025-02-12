A, B = map(int, input().split())

flag = True

if A < B:
    flag = False

x = (A + B) // 2
if x != (A + B) / 2:
    flag = False

y = abs(A - B) // 2
if y != abs(A - B) / 2:
    flag = False

if flag:
    print(x, y)
else: print(-1)
