from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        WATER, LAND = 0, 1
        max_island = 0

        def bfs(row, col):
            nonlocal max_island
            q = deque()
            q.append((row, col))
            grid[row][col] = WATER
            island_size = 1
            while q:
                row, col = q.popleft()
                for direction in directions:
                    nr, nc = row + direction[0], col + direction[1]
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == LAND:
                        q.append((nr, nc))
                        grid[nr][nc] = WATER
                        island_size += 1

            max_island = max(max_island, island_size)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND:
                    bfs(r, c)

        return max_island
