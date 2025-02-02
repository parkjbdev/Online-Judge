
def solution(n, results):
    arr = [[0 for _a in range(n)] for _b in range(n)]
    for winner, loser in results: arr[winner - 1][loser - 1] = 1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0 and arr[i][k] and arr[k][j]:
                    arr[i][j] = 1
    
    trans_arr = [list(x) for x in zip(*arr)]
    answer = 0
    
    for i in range(n):
        if sum(arr[i]) + sum(trans_arr[i]) == n - 1:
            answer += 1
    
    return answer