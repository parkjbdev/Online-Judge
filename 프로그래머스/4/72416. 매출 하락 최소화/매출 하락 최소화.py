nodes = None
dp = None

class Node:
    def __init__(self, me, parent, cost, childs):
        self.me = me
        self.parent = parent
        self.cost = cost
        self.childs = childs
        
    def __str__(self):
    	return f"node {self.me}: parent({self.parent}) cost({self.cost}) childs({self.childs})"
    
def dfs(node_id):
    node = nodes[node_id]
    if len(node.childs) == 0: return

    min_gap = float('inf')
    
    for child in node.childs:
        dfs(child)
        
        dp[node_id][0] += min(dp[child])
        dp[node_id][1] += min(dp[child])
        
        min_gap = min(min_gap, dp[child][1] - dp[child][0])
        min_gap = max(0, min_gap)
        
    dp[node_id][0] += min_gap

def solution(sales, links):
    global nodes, dp
    nodes = [Node(i, i, sale, set([])) for i, sale in enumerate(sales) ]
    
    for parent, child in links:
        nodes[parent - 1].childs.add(child - 1)
        nodes[child - 1].parent = parent - 1
        
    dp = [[0, sales[i]] for i in range(len(sales))]
    
    dfs(0)
    return min(dp[0])
