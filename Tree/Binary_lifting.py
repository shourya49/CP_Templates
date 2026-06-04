class BinaryLifting:

    def __init__(self, n, adj, root=0):

        self.n = n
        self.LOG = n.bit_length()

        self.up = [[-1] * self.LOG for _ in range(n)]

        self.build(adj, root)

    def build(self, adj, root):

        stack = [root]
        visited = [False] * self.n
        visited[root] = True

        while stack:

            node = stack.pop()

            for nei in adj[node]:

                if visited[nei]:
                    continue

                visited[nei] = True

                self.up[nei][0] = node

                for j in range(1, self.LOG):

                    parent = self.up[nei][j - 1]

                    if parent != -1:
                        self.up[nei][j] = self.up[parent][j - 1]

                stack.append(nei)

    def kth_parent(self, node, k):

        for j in range(self.LOG):

            if (k >> j) & 1:

                if node == -1:
                    return -1

                node = self.up[node][j]

        return node
    
n = 7

adj = [
    [1,2],
    [0,3,4],
    [0,5,6],
    [1],
    [1],
    [2],
    [2]
]

bl = BinaryLifting(n, adj, 0)

print(bl.kth_parent(4, 1))
print(bl.kth_parent(4, 2))

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
