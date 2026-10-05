import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            new_stone = stone1 - stone2
            if new_stone:
                heapq.heappush(max_heap, new_stone)

        return 0 if len(max_heap) == 0 else -heapq.heappop(max_heap)
