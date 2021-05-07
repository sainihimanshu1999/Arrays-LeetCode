'''
In this question, clever use fo stack is done
'''

def area(self,heights):
    stack = [-1]
    heights.append(0)

    area = 0

    for i,height in enumerate(heights):
        while heights[stack[-1]]>height:
            h = heights[stack.pop()]
            w = i-stack[-1]-1
            area = max(area, h*w)

        stack.append(i)

    return area