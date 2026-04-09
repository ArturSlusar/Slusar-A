class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        
        # Шаг 1: Ищем гнилые (в очередь) и считаем свежие
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
                    
        ans = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Направления: вправо, влево, вниз, вверх
        
        # Шаг 2: Запускаем BFS
        while q and fresh > 0:
            ans += 1
            # Обрабатываем ровно один "уровень" (одну минуту)
            for _ in range(len(q)):
                i, j = q.popleft()
                
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    # Если сосед - свежий апельсин
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2  # Гниет
                        fresh -= 1        # Свежих меньше
                        q.append((ni, nj))# В очередь на следующую минуту
                        
        return ans if fresh == 0 else -1