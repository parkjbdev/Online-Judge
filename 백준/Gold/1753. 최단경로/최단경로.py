from math import inf
import heapq

V, E = map(int, input().split())
K = int(input()) - 1

adj = [[] for _ in range(V)]

for _ in range(E):
    x, y, w = map(int, input().split())
    adj[x - 1].append((w, y - 1))

distance = [inf for _ in range(V)]
distance[K] = 0

heap = []
heapq.heappush(heap, (0, K))

while heap:
    # visit
    current_weight, current_vertex = heapq.heappop(heap)
    if distance[current_vertex] < current_weight:
        continue
    for adj_w, adj_v in adj[current_vertex]:
        new_distance = distance[current_vertex] + adj_w
        if new_distance < distance[adj_v]:
            distance[adj_v] = new_distance
            heapq.heappush(heap, (new_distance, adj_v))

print(*map(lambda x: str(x).upper(), distance), sep="\n")
