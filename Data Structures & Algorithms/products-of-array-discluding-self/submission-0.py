class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0] * n
        prefix_prods = [0] * n
        suffix_prods = [0] * n
        prefix_prods[0] = suffix_prods[n-1] = 1

        for i in range(1, n):
            prefix_prods[i] = nums[i - 1] * prefix_prods[i - 1]

        for i in range(n - 2, -1, -1):
            suffix_prods[i] = nums[i + 1] * suffix_prods[i + 1]
        
        for i in range(n):
            out[i] = (prefix_prods[i] * suffix_prods[i])
            
        return out
            
