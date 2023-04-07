class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:       
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if image[sr][sc] == color:
            return image
        original_color = image[sr][sc]

        def inBound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        def dfs(row, col):
            if not inBound(row, col) or image[row][col] != original_color:
                return 

            image[row][col] = color

            for dx, dy in directions:
                dfs(row + dx, col + dy)

        dfs(sr, sc)

        return image
