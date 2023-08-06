from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for value in row] for row in grid]
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col]:
                    continue
                elif grid[row][col] == "1":
                    self.traverseNode(row, col, grid, visited)
                    count += 1

        return count

    def traverseNode(self, row, col, grid, visited):
        if row < 0 or row > len(grid) - 1:
            return
        if col < 0 or col > len(grid[0]) - 1:
            return
        if visited[row][col]:
            return
        visited[row][col] = True
        if grid[row][col] != "1":
            return

        grid[row][col] = "2"

        self.traverseNode(row+1, col, grid, visited)
        self.traverseNode(row-1, col, grid, visited)
        self.traverseNode(row, col+1, grid, visited)
        self.traverseNode(row, col-1, grid, visited)
