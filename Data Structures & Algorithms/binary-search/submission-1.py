class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_mid(h, l) -> int:
            return int(l + (h - l) // 2)

        high = len(nums)
        low = 0
        mid = get_mid(high, low)
        num = nums[mid]
        while num != target:
            if num > target:
                high = mid
            elif num < target:
                low = mid

            prev_mid = mid
            mid = get_mid(high, low)
            if prev_mid == mid:
                break
            num = nums[mid]

        if nums[mid] != target:
            return -1
        return mid