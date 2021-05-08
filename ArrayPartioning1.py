'''
nums[::k] jumps k place
'''
def arrayPairSum(self,nums):
    nums.sort()
    return sum(nums[::2])
