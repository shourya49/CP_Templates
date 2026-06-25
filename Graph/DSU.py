class DSU:
    def __init__(self, n):
        # Initially every node is its own parent
        self.parent = list(range(n))

        # Rank = approximate tree height
        self.rank = [0] * n

    def find(self, x):
        # If x is not the root
        if self.parent[x] != x:
            # Path Compression:
            # Make x directly point to the ultimate root
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        # Already in same component
        if root_u == root_v:
            return

        # Attach smaller rank tree under larger rank tree
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v

        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u

        else:
            # Same rank
            self.parent[root_v] = root_u
            self.rank[root_u] += 1


dsu = DSU(5)

dsu.union(0, 1)
dsu.union(1, 2)

print(dsu.find(0))  # root
print(dsu.find(2))  # same root

print(dsu.find(3))  # separate component
