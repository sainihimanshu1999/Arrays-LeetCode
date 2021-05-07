'''
Just have to return the exact ith value not the whole triangle
'''
def pascalTriangle(self,rowIndex):
    dp = [[1]*(i+1) for i in range(rowIndex+1)]

    for i in range(rowIndex+1):
        for j in range(1,i):
            dp [i][j] = dp[i-1][j-1]+ dp[i-1][j]

    return dp[-1]