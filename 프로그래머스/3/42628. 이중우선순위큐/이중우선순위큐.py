from collections import deque

def solution(operations):
    q = deque([])
    
    for op in operations:
        opcode, opnum = op.split()
        opnum = int(opnum)
        
        if opcode == "I":
            # insert number
            # q.append(opnum)
            # q.sort()
            if not q:
                q.append(opnum)
                continue
            elif opnum < q[0]: 
                q.appendleft(opnum)
                continue
            elif opnum > q[-1]: 
                q.append(opnum)
                continue
            
            # 이분탐색 어떰?
            start, end = 0, len(q) - 1
            while start < end - 1:
                idx = (start + end) // 2
                if q[idx] < opnum: start = idx
                else: end = idx
            q.insert(end, opnum)
            
        elif opcode == "D" and opnum > 0:
            # delete max from queue
            if q: q.pop()
            else: continue
        elif opcode == "D" and opnum < 0:
            # delete min from queue
            if q: q.popleft()
            else: continue
    
    if q: return [q[-1], q[0]]
    else: return [0,0]