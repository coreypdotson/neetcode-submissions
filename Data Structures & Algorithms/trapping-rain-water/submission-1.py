class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_area = 0
        l = 0
        r = 0
        l_vals = [0] * n
        r_vals = [0] * n

        for i in range(n):
            l = max(l, height[i])
            r = max(r, height[n - i - 1])
            l_vals[i] = l
            r_vals[n - i - 1] = r

        for i in range(n):
            total_area += max(min(l_vals[i], r_vals[i]) - height[i], 0)
        return total_area