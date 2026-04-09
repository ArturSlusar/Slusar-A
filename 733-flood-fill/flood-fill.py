class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_c = image[sr][sc]

        # Если перекрашивать не нужно, сразу выходим
        if old_c == color:
            return image

        m = len(image)
        n = len(image[0])

        def dfs(i, j):
            # Проверка выхода за границы и совпадения цвета
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != old_c:
                return
            
            # Красим
            image[i][j] = color

            # Идем в 4 стороны
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        dfs(sr, sc)
        return image