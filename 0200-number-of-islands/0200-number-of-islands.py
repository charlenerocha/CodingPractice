class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        num_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        # start with first unseen in grid
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in self.visited and grid[i][j] == '1':
                    # collect that island
                    num_islands += 1
                    self.collect_island(i, j, grid, rows, cols)     

        return num_islands

    def collect_island(self, i, j, grid, rows, cols):
        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == '1' and (i, j) not in self.visited:
            self.visited.add((i, j))
            self.collect_island(i+1, j, grid, rows, cols)
            self.collect_island(i-1, j, grid, rows, cols)
            self.collect_island(i, j+1, grid, rows, cols)
            self.collect_island(i, j-1, grid, rows, cols)
