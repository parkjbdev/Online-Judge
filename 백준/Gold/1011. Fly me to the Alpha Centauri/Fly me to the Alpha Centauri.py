from math import sqrt


def solve(distance):
    n = int(sqrt(distance - 1))
    return 2 * n + int(distance / (n**2 + n + 1))

T = int(input())

test_cases = []

for i in range(T):
    inputs = input().split(' ')
    test_cases.append(int(inputs[1]) - int(inputs[0]))

for test_case in test_cases:
    print(solve(test_case))
