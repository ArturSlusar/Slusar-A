class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        ans = 0

        def dfs(i, j):
            # Если вышли за границы или попали в воду — выходим
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return

            # Топим сушу
            grid[i][j] = '0'
            
            # Обходим всех соседей
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        return ans