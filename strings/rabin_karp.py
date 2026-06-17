def rabin_karp(text, pattern):

    n = len(text)
    m = len(pattern)

    if m > n:
        return False

    base = 256
    mod = 10**9 + 7

    pattern_hash = 0
    window_hash = 0

    power = pow(base, m-1, mod)

    # build hashes
    for i in range(m):
        pattern_hash = (
            pattern_hash * base + ord(pattern[i])
        ) % mod

        window_hash = (
            window_hash * base + ord(text[i])
        ) % mod

    # slide window
    for start in range(n - m + 1):

        if pattern_hash == window_hash:
            if text[start:start+m] == pattern:
                return True

        if start < n - m:

            # remove left char
            window_hash = (
                window_hash
                - ord(text[start]) * power
            ) % mod

            # shift and add right char
            window_hash = (
                window_hash * base
                + ord(text[start + m])
            ) % mod

    return False
