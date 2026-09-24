class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
                 /\
                9  []
                /\
                2 []

        """
        res = []
        candidates.sort()

        combination = []

        def dfs(i: int, total: int):
            if total == target:
                res.append(combination.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # Decision Tree
            combination.append(candidates[i])
            dfs(i + 1, candidates[i] + total)

            combination.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)


        dfs(0, 0)
        return res