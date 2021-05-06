'''
In this question we are editing grid in place, first taking first coloumn traversing cost,
then taking first row traversing cost and then adding minimum of both to the destination
'''

def minimumPathsum(self,grid):
    row = len(grid)
    col = len(grid[0])

    for i in range(1,row):
        grid[i][0] += grid[i-1][0]

    for i in range(1,col):
        grid[0][i] += grid[0][i-1]


    for i in range(1,row):
        for j in range(1,col):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[-1][-1]