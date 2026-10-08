from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        LAND = '1'
        WATER = '0'

        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = WATER
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == WATER):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = WATER
            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == LAND:
                    islands += 1
                    bfs(r, c)

        return islands