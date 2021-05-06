def uniquePaths2(self,obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0]*n for i in range(m)]
    dp[0][0] = 1 if obstacleGrid[0][0]==0 else 0

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j]==1:
                dp[i][j] = 0

            else:
                if i-1>=0:
                    dp[i][j]  += dp[i-1][j]

                if j-1>=0:
                    dp[i][j] += dp[i][j-1]
    return dp[-1][-1]