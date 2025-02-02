def solution(n):
    q, r = divmod((n - 1),  3)
    return '124'[r] if q == 0 else solution(q) + '124'[r]