class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_prime = "#" + "#".join(s) + "#"
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = right_boundary = 0

        # Iterate through s_prime
        for i in range(n):
            mirror = 2 * center - i

            # Mirror if within range
            if i < right_boundary:
                palindrome_radii[i] = min(right_boundary - i, palindrome_radii[mirror])

            # Expand
            while (
                i + 1 + palindrome_radii[i] < n
                and i - 1 - palindrome_radii[i] >= 0
                and s_prime[i + 1 + palindrome_radii[i]]
                == s_prime[i - 1 - palindrome_radii[i]]
            ):
                palindrome_radii[i] += 1

            # Update center and right_boundary
            if i + palindrome_radii[i] > right_boundary:
                center = i
                right_boundary = i + palindrome_radii[i]

        max_length = max(palindrome_radii)
        center_index = palindrome_radii.index(max_length)
        start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index : start_index + max_length]

        return longest_palindrome
