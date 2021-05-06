'''
Basic tabulation method is used in this question
'''

def uniquePaths(self,m,n):
    if not m or not n:
        return 0

    grid = [[1]*n for i in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            grid[i][j] = grid[i-1][j]+grid[i][j-1]
    
    return grid[-1][-1]