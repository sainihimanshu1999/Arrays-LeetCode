'''
In this question, first we calculate the if the new row size and col size given can take original
matrix, if yes then we proceed futher
'''

def reshapeMat(self,grid,row,col):
    if len(grid)*len(grid[0] != row*col:
        return grid


    vals = [val for row in grid for val in row]
    ret = [[None]*col for _ in range(row)]

    i = 0
    for r in range(row):
        for c in range(col):
            ret[r][c] = vals[i]
            i+=1

    return ret
