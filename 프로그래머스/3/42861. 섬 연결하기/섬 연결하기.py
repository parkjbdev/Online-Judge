parent = None

def find(x):
    return x if x == parent[x] else find(parent[x])

def union(a, b):
    a = find(a)
    b = find(b)
    
    parent[b] = a
    
def kruskal(n, costs):
    global parent
    parent = [i for i in range(n)]
    costs.sort(key=lambda x:x[2])
    answer = 0
    
    for v1, v2, c in costs:
        if find(v1) != find(v2):
            union(v1, v2)
            answer += c
            
    return answer

from heapq import *

def prim(n, costs):
    answer = 0
    
    # init adjacents
    adj_edges = [[] for _ in range(n)]
    for v1, v2, c in costs:
        adj_edges[v1].append((c, v2))
        adj_edges[v2].append((c, v1))
    
    # init visited
    visited = [False for _ in range(n)]
    visited[0] = True
    
    # init candidates
    candidate_edges = adj_edges[0]
    heapify(candidate_edges)
    
    while candidate_edges:
        c, v = heappop(candidate_edges)
        if not visited[v]:
            visited[v] = True
            answer += c
            for edge in adj_edges[v]:
                if not visited[edge[1]]:
                    heappush(candidate_edges, edge)
    
    return answer
    
def solution(n, costs):
    fun = None
    
    if n > 10: fun = prim
    else: fun = kruskal
    
    return fun(n, costs)