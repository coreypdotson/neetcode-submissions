class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combination, total):
            if total == target:
                res.append(combination.copy())
                return
            elif i >= len(nums) or total > target:
                return
            
            combination.append(nums[i])
            dfs(i, combination, nums[i] + total)

            combination.pop()
            dfs(i + 1, combination, total)

        dfs(0, [], 0)

        return res