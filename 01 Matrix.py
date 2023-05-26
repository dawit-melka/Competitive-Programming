class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()
        visited = set()
        def inBound(row, col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                    visited.add((row, col))

        while queue:
            row, col,  dis = queue.popleft()
            mat[row][col] = dis
            
            for dx, dy in directions:
                r, c = row + dx, col + dy
                if inBound(r, c) and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, dis + 1))
        
        return mat
