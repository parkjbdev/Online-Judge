from collections import deque
from heapq import *

def solution(jobs):
    jobs.sort()
    jobs = deque(jobs)
    
    length = len(jobs)
    current_time = 0
    elapsed_time = 0
    
    done_jobs = 0
    queue = []
    heapify(queue)
    
    while done_jobs < length:
        for start, elapse in jobs.copy():
            if start > current_time: break
            heappush(queue, (elapse, start))
            jobs.popleft()
        
        if len(queue) == 0: 
            current_time += 1
            continue
        
        elapse, start = heappop(queue)
        current_time += elapse
        elapsed_time += current_time - start
        done_jobs += 1
    
    return elapsed_time // length