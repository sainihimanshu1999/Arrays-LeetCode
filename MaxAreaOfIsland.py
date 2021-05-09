'''
using dfs
'''

def maxArea(Self,grid):
    row = len(grid)
    col = len(grid[0])

    def dfs(i,j):
        if 0<=i<row and 0<=j<col and grid[i][j]:
            grid[i][j] = 0
            return 1+dfs(i+1,j)+dfs(i,j+1),dfs(i-1,j)+dfs(i,j-1)
        return 0

    areas = [dfs(i,j) for i in range(row) for j in range(col) if grid[i][j]]

    return max(areas) if areas else 0