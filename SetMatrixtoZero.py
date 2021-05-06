'''
In this question we have to set the matrix element(boht row and col zero) where zero is originally present
we make two list rl and cl and same row and col coordinate where zero appears, and then remove duplicates
from them and make every element of row and col zero there
'''

def setmatrixzero(self,matrix):
    m = len(matrix)
    n = len(matrix[0])

    rl = []
    cl = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                rl.append(i)
                cl.append(j)


    rs = list(set(rl))
    cs = list(set(cl))

    while len(rs)>0:
        row = rs.pop()
        for j in range(n):
            matrix[row][j] = 0

    while len(cs)>0:
        col = cs.pop()
        for i in range(m):
            matrix[i][col] = 0

    return matrix