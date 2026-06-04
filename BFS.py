from collections import deque
import sys

def solve():
    # 1. FAST I/O READ
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # 2. BUILD GRAPH (1-indexed)
    graph = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        graph[u].append(v)
        graph[v].append(u)
        idx += 2
        
    # 3. BFS TRACKING ARRAYS
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    dp = [1] * (n + 1)       # dp[i] will store the size of the subtree rooted at i
    order = []              # Saves the top-down layer order
    
    # 4. BFS TRAVERSAL ENGINE (Top-Down Layering)
    root = 1                # Change this if the problem specifies a different root
    queue = deque([root])
    
    while queue:
        curr = queue.popleft()
        order.append(curr)
        
        for neighbor in graph[curr]:
            if neighbor != parent[curr]:
                parent[neighbor] = curr
                depth[neighbor] = depth[curr] + 1
                queue.append(neighbor)
                
    # 5. BOTTOM-UP DP ENGINE (Computes Subtree Sizes)
    for node in reversed(order):
        if node != root:
            p = parent[node]
            dp[p] += dp[node]  # Add child's subtree size to its parent

    # =================================================================
    # YOUR ADDITIONAL LOGIC GOES HERE
    # =================================================================
    # Property 1: parent[i] -> parent of node i
    # Property 2: depth[i]  -> distance from the root
    # Property 3: dp[i]     -> total nodes in node i's subtree (fully computed!)
    #
    # If you need an extra top-down pass (like rerooting DP):
    # for node in order:
    #     if node != root:
    #         p = parent[node]
    #         ...
    # =================================================================

if __name__ == '__main__':
    solve()
