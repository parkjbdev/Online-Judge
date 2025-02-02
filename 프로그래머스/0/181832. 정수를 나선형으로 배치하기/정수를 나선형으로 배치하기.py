def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    value = 1
    x, y = 0, -1
    adder = 1
    
    while value <= n ** 2:
        while 0 <= y + adder < n and answer[x][y + adder] == 0:
            y += adder
            answer[x][y] = value
            value += 1
            
        if value > n ** 2: break
            
        while 0 <= x + adder < n  and answer[x + adder][y] == 0:
            x += adder
            answer[x][y] = value
            value += 1
        
        adder = -adder
        
    return answer