class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        max_len = 0
        max_f = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_f = max(max_f, counts[s[r]])

            while (r - l + 1) - max_f > k:
                counts[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len