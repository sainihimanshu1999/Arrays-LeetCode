'''
This is a universal way of finding the subset
'''

def subsets(self,nums):
    if not nums:
        return []

    x = [[]]

    for i in range(len(nums)):
        for j in range(len(x)):
            x.append(x[j]+[nums[i]])


    return x