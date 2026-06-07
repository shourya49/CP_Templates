import sys

def main():
    # Fast I/O: Read all inputs from standard input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Map all string tokens to integers using optimized C-level functions
    data = list(map(int, input_data))
    
    n = data[0]
    
    # Build a 0-indexed adjacency list
    adj = [[] for _ in range(n)]
    idx = 1
    for _ in range(n - 1):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # Step 1: Iterative DFS to flatten the tree
    # This generates a topological/post-order processing sequence without recursion
    order = []
    parent = [-1] * n
    stack = [0]  # Start DFS from root (0)
    
    while stack:
        curr = stack.pop()
        order.append(curr)
        p_curr = parent[curr]
        for neighbor in adj[curr]:
            if neighbor != p_curr:
                parent[neighbor] = curr
                stack.append(neighbor)
                
    # Step 2: Calculate subtree sizes bottom-up
    # Processes leaves first, moving up to the root safely
    subtree_size = [1] * n
    for node in reversed(order):
        p = parent[node]
        if p != -1:
            subtree_size[p] += subtree_size[node]
            
    # Step 3: Iterative Centroid Search
    # Start at the root and move down to any child that contains more than half the nodes
    curr = 0
    while True:
        moved = False
        p_curr = parent[curr]
        for neighbor in adj[curr]:
            if neighbor != p_curr:
                # If a child's component has a size greater than N // 2,
                # the centroid must be further down inside that child's subtree
                if subtree_size[neighbor] * 2 > n:
                    curr = neighbor
                    moved = True
                    break  # Move to this neighbor and restart the check
                    
        # If no child component takes up more than half the tree, 'curr' is a valid centroid
        if not moved:
            print(curr + 1)  # Convert back to 1-based indexing for CSES
            break

if __name__ == "__main__":
    main()
