def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 0
    last_cam = -30001
    
    for start, end in routes:
        if not (start <= last_cam and last_cam <= end):
            last_cam = end
            answer += 1
    
    return answer