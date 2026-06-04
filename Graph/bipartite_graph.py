from collections import deque

def is_bipartite(n, adj):
    color = [-1] * n

    for start in range(n):

        if color[start] != -1:
            continue

        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()

            for nei in adj[node]:

                if color[nei] == -1:
                    color[nei] = color[node] ^ 1
                    queue.append(nei)

                elif color[nei] == color[node]:
                    return False

    return True
