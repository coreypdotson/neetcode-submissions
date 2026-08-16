class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_mid(low, high) -> int:
            return int(low + (high - low) // 2)

        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m * n - 1
        
        while l <= r:
            mid = get_mid(l, r)
            row = mid // n
            col = mid % n
            num = matrix[row][col]
            
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False