from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        counts = Counter(nums)

        out = []
        for i, target in enumerate(nums):
            counts[target] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                counts[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if counts[target] > 0:
                    out.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                counts[nums[j]] += 1                
        return out