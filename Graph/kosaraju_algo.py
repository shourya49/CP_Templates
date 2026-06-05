from collections import deque

def kosaraju(n, adj):

    rev_adj = [[] for _ in range(n)]

    for u in range(n):
        for v in adj[u]:
            rev_adj[v].append(u)

    # ---------- First Pass ----------
    vis = [False] * n
    order = []

    for start in range(n):

        if vis[start]:
            continue

        stack = [(start, 0)]
        vis[start] = True

        while stack:

            node, idx = stack[-1]

            if idx < len(adj[node]):

                nei = adj[node][idx]
                stack[-1] = (node, idx + 1)

                if not vis[nei]:
                    vis[nei] = True
                    stack.append((nei, 0))

            else:
                order.append(node)
                stack.pop()

    # ---------- Second Pass ----------
    vis = [False] * n
    sccs = []

    while order:

        start = order.pop()

        if vis[start]:
            continue

        component = []

        stack = [start]
        vis[start] = True

        while stack:

            node = stack.pop()
            component.append(node)

            for nei in rev_adj[node]:

                if not vis[nei]:
                    vis[nei] = True
                    stack.append(nei)

        sccs.append(component)

    return sccs

n = 5

adj = [
    [1],
    [2],
    [0,3],
    [4],
    [3]
]

sccs = kosaraju(n, adj)

for comp in sccs:
    print(comp)
