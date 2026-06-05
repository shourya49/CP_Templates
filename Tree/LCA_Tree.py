import sys
input = sys.stdin.readline

n = int(input())

LOG = n.bit_length()

adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())

    adj[u].append(v)
    adj[v].append(u)

up = [[0] * LOG for _ in range(n + 1)]
depth = [0] * (n + 1)

# ---------- Build Binary Lifting Table ----------

root = 1

stack = [(root, 0)]

while stack:

    node, parent = stack.pop()

    up[node][0] = parent

    for j in range(1, LOG):
        up[node][j] = up[up[node][j - 1]][j - 1]

    for nei in adj[node]:

        if nei == parent:
            continue

        depth[nei] = depth[node] + 1
        stack.append((nei, node))

# ---------- LCA ----------

def lca(a, b):

    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]

    # bring a to same depth as b
    for j in range(LOG):

        if diff & (1 << j):
            a = up[a][j]

    if a == b:
        return a

    # lift both together
    for j in range(LOG - 1, -1, -1):

        if up[a][j] != up[b][j]:

            a = up[a][j]
            b = up[b][j]

    return up[a][0]

# ---------- Queries ----------

q = int(input())

for _ in range(q):

    a, b = map(int, input().split())

    print(lca(a, b))
