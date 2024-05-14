from typing import List


class PathWithMaximumGold:
    def __init__(self):
        self.maxGold = None
        self.directions = None

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0

        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.maxGold = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 0:
                    self.dfs(grid, row, col, 0)
        return self.maxGold

    def dfs(self, grid, x, y, cur):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] <= 0:
            return
        cur += grid[x][y]
        self.maxGold = max(self.maxGold, cur)
        temp = grid[x][y]
        grid[x][y] = 0

        for dx, dy in self.directions:
            self.dfs(grid, x + dx, y + dy, cur)

        grid[x][y] = temp

# class Solution:
#     def getMaximumGold(self, grid: List[List[int]]) -> int:
#         nRows, nCols = len(grid), len(grid[0])
#         visited = set()
#
#         def inBound(row, col):
#             return 0 <= row < nRows and 0 <= col < nCols
#
#         def dfs(row, col):
#             if not inBound(row, col) or (row, col) in visited or grid[row][col] == 0:
#                 return 0
#
#             visited.add((row, col))
#
#             left = dfs(row, col - 1)
#             right = dfs(row, col + 1)
#             up = dfs(row - 1, col)
#             down = dfs(row + 1, col)
#
#             visited.remove((row, col))
#
#             return grid[row][col] + max(left, right, up, down)
#
#         maxGold = 0
#
#         for row in range(nRows):
#             for col in range(nCols):
#                 if grid[row][col] and (row, col) not in visited:
#                     maxGold = max(maxGold, dfs(row, col))
#
#         return maxGold