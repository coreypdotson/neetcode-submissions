from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = deque()
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, pos = stack.pop()
                res[pos] = i - pos
            stack.append((temp, i))
        return res