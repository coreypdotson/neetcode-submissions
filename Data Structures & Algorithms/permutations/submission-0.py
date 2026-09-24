class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            [1,2,3,4]
                 1  repeat for [2, 3, 4]
                /|\
               2 3 4
              /\ /\ /\  
             3 4 2 43 2
             | | | | | |
             4 3 4 2 2 3


             O(n! * n)
        """
        res = []

        def backtrack(perm: List[int], pick: List[bool]):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(perm, pick)
                    perm.pop()
                    pick[i] = False

        backtrack([], [False] * len(nums))

        return res