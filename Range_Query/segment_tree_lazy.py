# Segment Tree with Lazy Propagation
# Range Add Update + Range Sum Query

n = len(arr)
tree = [0] * (4 * n)
lazy = [0] * (4 * n)

def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2
    build(2 * node, start, mid)
    build(2 * node + 1, mid + 1, end)

    tree[node] = tree[2 * node] + tree[2 * node + 1]

def push(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]

        if start != end:
            lazy[2 * node] += lazy[node]
            lazy[2 * node + 1] += lazy[node]

        lazy[node] = 0

def update(node, start, end, left, right, value):
    push(node, start, end)

    if right < start or end < left:
        return

    if left <= start and end <= right:
        lazy[node] += value
        push(node, start, end)
        return

    mid = (start + end) // 2

    update(2 * node, start, mid, left, right, value)
    update(2 * node + 1, mid + 1, end, left, right, value)

    tree[node] = tree[2 * node] + tree[2 * node + 1]

def query(node, start, end, left, right):
    push(node, start, end)

    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    return (
        query(2 * node, start, mid, left, right)
        + query(2 * node + 1, mid + 1, end, left, right)
    )

# build(1, 0, n - 1)
