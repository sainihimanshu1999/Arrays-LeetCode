'''
We just make an array of 3 elements and add up elements from num under certain conditions
'''

def thirdMax(self,nums):
    a = [float('-inf'),float('-inf'),float('-inf')]
    for num in nums:
        if num not in a:
            if num>a[0]:
                a = [num,a[0],a[1]]

            elif num>a[1]:
                a = [a[0],num,a[1]]

            elif num>a[2]:
                a = [a[0],a[1],num]

    return max(nums) if float('-inf') in a else a[2]