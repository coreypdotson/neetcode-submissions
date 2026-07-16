class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        ans = [-1, -1]

        for i, num in enumerate(nums):
            if num in hashmap:
                ans = [hashmap.get(num), i]
                break
            else:
                hashmap[target - num] = i

        return ans