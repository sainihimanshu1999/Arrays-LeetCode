'''
In this question, we will move in the matrix and keep adding numbers
'''

def spiral(self,n):
    if not n:
        return []

    matrix = [[0]*n for i in range(n)]

    left,right = 0,n-1
    top,down = 0,n-1
    num = 1

    while left<=right and top<=down:
        for i in range(left,right):
            matrix[top][i] = num
            num += 1
        top +=1
        for i in range(top,down):
            matrix[i][right] = num
            num += 1
        right -=1
        for i in range(right,left-1,-1):
            matrix[down][i] = num
            num += 1
        down -=1
        for i in range(down,top-1,-1):
            matrix[i][left] = num
            num +=1
        left += 1
    return matrix