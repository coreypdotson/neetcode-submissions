import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_mid(low, high) -> int:
            return (high + low) // 2

        l = 1
        r = max(piles) # O(n)
        res = r

        while l <= r:
            k = get_mid(l, r)

            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / k)
            if total_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

