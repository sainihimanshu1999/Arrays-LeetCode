'''
This question was pretty tricky to understand but it is done using the same logic of largest area
in histogram. Heights array si created by calculating the consecustive one's present in the row
'''

def maximalArea(self,matrix):
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix[0])
    heights = [0]*(n+1)

    area = 0

    for row in matrix:
        for i in range(n):
            heights[i] = heights[i]+1 if row[i]=='1' else 0

        stack = [-1]
        for i, height in enumerate(heights):
            while heights[stack[-1]]>height:
                h = height[stack.pop()]
                w = i-stack[-1]-1
                area = max(area,h*w)

    return area