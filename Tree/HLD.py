import sys
input = sys.stdin.readline

# --------------------------------------------------
# parent[node] = parent of node
# depth[node]  = depth from root
#
# sz[node]     = subtree size
# heavy[node]  = child with maximum subtree size
#
# head[node]   = head of heavy chain containing node
# pos[node]    = position of node in HLD order
# --------------------------------------------------

def build_hld(n, adj, root=1):

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)

    sz = [1] * (n + 1)
    heavy = [0] * (n + 1)

    head = [0] * (n + 1)
    pos = [0] * (n + 1)

    # ---------- DFS ORDER ----------
    # computes parent and depth

    order = []
    stack = [root]

    parent[root] = -1

    while stack:

        node = stack.pop()
        order.append(node)

        for nxt in adj[node]:

            if nxt == parent[node]:
                continue

            parent[nxt] = node
            depth[nxt] = depth[node] + 1

            stack.append(nxt)

    # ---------- SUBTREE SIZES ----------
    # computes sz[] and heavy[]

    for node in reversed(order):

        mx = 0

        for nxt in adj[node]:

            if nxt == parent[node]:
                continue

            sz[node] += sz[nxt]

            if sz[nxt] > mx:
                mx = sz[nxt]
                heavy[node] = nxt

    # ---------- DECOMPOSITION ----------
    # assigns head[] and pos[]

    timer = 1

    stack = [(root, root)]  # (node, chain_head)

    while stack:

        node, h = stack.pop()

        while node:

            head[node] = h
            pos[node] = timer

            timer += 1

            for nxt in adj[node]:

                if nxt != parent[node] and nxt != heavy[node]:
                    stack.append((nxt, nxt))

            node = heavy[node]

    return parent, depth, sz, heavy, head, pos


# ---------- BIT ----------
# node value of u is stored at pos[u]

def build_bit(n):

    bit = [0] * (n + 1)

    def update(idx, val):

        while idx <= n:
            bit[idx] += val
            idx += idx & -idx

    def query(idx):

        ans = 0

        while idx:
            ans += bit[idx]
            idx -= idx & -idx

        return ans

    def range_query(l, r):
        return query(r) - query(l - 1)

    return update, query, range_query


# ---------- PATH QUERY ----------
# Query path u -> v

def path_query(u, v, parent, depth, head, pos, range_query):

    ans = 0

    while head[u] != head[v]:

        # keep u on deeper chain
        if depth[head[u]] < depth[head[v]]:
            u, v = v, u

        ans += range_query(
            pos[head[u]],
            pos[u]
        )

        u = parent[head[u]]

    # now both nodes are in same chain

    if depth[u] > depth[v]:
        u, v = v, u

    ans += range_query(
        pos[u],
        pos[v]
    )

    return ans


# ---------------- Example Usage ----------------

n = int(input())

adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):

    u, v = map(int, input().split())

    adj[u].append(v)
    adj[v].append(u)

parent, depth, sz, heavy, head, pos = build_hld(n, adj)

update, query, range_query = build_bit(n)

# value[u] should be stored at pos[u]
# update(pos[u], value)

# path sum between u and v
# ans = path_query(u, v, parent, depth, head, pos, range_query)
