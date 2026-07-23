class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        def getArea(left: int, right: int) -> int:
            return min(heights[left], heights[right]) * (right - left)

        while l < r:
            max_area = max(max_area, getArea(l, r))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_area