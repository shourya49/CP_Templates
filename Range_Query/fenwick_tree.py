# Fenwick Tree / BIT
# Point Update + Prefix Sum Query

n = len(arr)
bit = [0] * (n + 1)

def add(idx, value):
    idx += 1

    while idx <= n:
        bit[idx] += value
        idx += idx & -idx

def prefix_sum(idx):
    idx += 1
    result = 0

    while idx > 0:
        result += bit[idx]
        idx -= idx & -idx

    return result

def range_sum(left, right):
    return prefix_sum(right) - prefix_sum(left - 1)

def build():
    for i in range(n):
        add(i, arr[i])

# build()
