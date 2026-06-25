n = 10

parent = list(range(n))
rank = [0] * n      # for union by rank
size = [1] * n      # for union by size


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])   # Path Compression
    return parent[x]


# --------------------------------
# Union by Rank
# --------------------------------
def union_by_rank(u, v):
    pu = find(u)
    pv = find(v)

    if pu == pv:
        return False

    if rank[pu] < rank[pv]:
        parent[pu] = pv

    elif rank[pu] > rank[pv]:
        parent[pv] = pu

    else:
        parent[pv] = pu
        rank[pu] += 1

    return True


# --------------------------------
# Union by Size
# --------------------------------
def union_by_size(u, v):
    pu = find(u)
    pv = find(v)

    if pu == pv:
        return False

    if size[pu] < size[pv]:
        pu, pv = pv, pu

    parent[pv] = pu
    size[pu] += size[pv]

    return True

# Check if two nodes belong to same component
def same(u, v):
    return find(u) == find(v)


# Size of component containing node x
def component_size(x):
    return size[find(x)]


union_by_size(0, 1)
union_by_size(1, 2)

print(find(0))
print(find(2))
print(component_size(0))   # 3
