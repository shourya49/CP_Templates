
LOG = n.bit_length()

up = [[0] * LOG for _ in range(n + 1)]

root = 1

stack = [root]
vis = [False] * (n + 1)
vis[root] = True

while stack:

    node = stack.pop()

    for nei in adj[node]:

        if vis[nei]:
            continue

        vis[nei] = True
        up[nei][0] = node

        stack.append(nei)

for j in range(1, LOG):
    for node in range(1, n + 1):
        up[node][j] = up[up[node][j - 1]][j - 1]

def kth_ancestor(node, k):

    for j in range(LOG):

        if k & (1 << j):
            node = up[node][j]

            if node == 0:
                break

    return node
