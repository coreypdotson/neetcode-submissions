class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        EMPTY_CHAR = "."
        board_size = len(board)
    
        rows = [0] * board_size
        cols = [0] * board_size
        squares = [0] * board_size

        for r in range(board_size):
            for c in range(board_size):
                if board[r][c]== EMPTY_CHAR:
                    continue
                val = int(board[r][c]) - 1
                mask_val = (1 << val)
                square_loc = (r // 3) * 3 + (c // 3)

                if rows[r] & mask_val:
                    return False
                if cols[c] & mask_val:
                    return False
                if squares[square_loc] & mask_val:
                    return False
                
                rows[r] |= mask_val
                cols[c] |= mask_val
                squares[square_loc] |= mask_val

        return True