class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            l_num = numbers[l]
            r_num = numbers[r]
            current_sum = l_num + r_num
            if current_sum == target:
                return [l + 1, r + 1]
            elif current_sum >= target:
                r -= 1
            elif current_sum <= target:
                l += 1
            