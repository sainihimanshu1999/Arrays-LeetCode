'''
In this question we edit the array in-place, we mark the the numbers negative and when the numbers are
positive those index+1 numbers are missing
'''

def disappeared(self,nums):
    for i in range(len(nums)):
        idx = abs(nums[i])-1
        nums[idx] = -abs(nums[idx])
    return [i+1 for i in range(len(nums)) if nums[i]>0]