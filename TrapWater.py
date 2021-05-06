'''
This question is pretty hard but straighforward, answer is based upon getting max left and max right height
of buildings, because water will accumlate according to the minimum height of building in left or right, and
then we substract the height of the building we are currently on. to get the water present there
'''

def TrapWater(self,height):
    leftmaxheight = [0]*len(height)
    rightmaxheight = [0]*len(height)

    water = [0]*len(height)
    maxLeft = 0
    maxRight = 0


    for i in range(len(height)):
        maxLeft = max(maxLeft, height[i])
        leftmaxheight[i] = maxLeft

    for i in range(len(height))[::-1]:
        maxRight = max(maxRight,height[i])
        rightmaxheight[i] = maxRight

    for i in range(len(height)):
        water[i] = min(leftmaxheight[i],rightmaxheight[i])-height[i]

    return sum(water)