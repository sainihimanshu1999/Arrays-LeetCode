'''
Only thing to remember in pascal triangle is (i,j) = (i-1)(j-1)+(i-1)(j)
'''

def pascaltriangle(self,num):
    dp = [[1]*(i+1) for i in range(num)]
    for i in range(num):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp