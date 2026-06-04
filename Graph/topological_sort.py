from collections import deque

def topo_sort(n, edges):
    adj = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    queue = deque()

    for node in range(n):
        if indegree[node] == 0:
            queue.append(node)

    topo = []

    while queue:
        node = queue.popleft()
        topo.append(node)

        for nei in adj[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                queue.append(nei)

    if len(topo) != n:
        return []

    return topo
