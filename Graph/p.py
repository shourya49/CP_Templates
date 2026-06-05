from heapq import heappush, heappop

INF = float('inf')

def dijkstra(n, adj, source):

    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)

    dist[source] = 0

    pq = [(0, source)]

    while pq:

        d, node = heappop(pq)

        if d > dist[node]:
            continue

        for nei, wt in adj[node]:

            nd = d + wt

            if nd < dist[nei]:

                dist[nei] = nd
                parent[nei] = node

                heappush(pq, (nd, nei))

    return dist, parent


def get_path(parent, destination):

    path = []

    while destination != -1:
        path.append(destination)
        destination = parent[destination]

    path.reverse()

    return path

n = 5

adj = [[] for _ in range(n + 1)]

edges = [
    (1, 2, 2),
    (1, 3, 4),
    (2, 3, 1),
    (2, 4, 7),
    (3, 5, 3),
    (4, 5, 1)
]

for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))      # remove for directed graph

dist, parent = dijkstra(n, adj, 1)

print(dist[5])                # shortest distance

print(get_path(parent, 5))    # shortest path