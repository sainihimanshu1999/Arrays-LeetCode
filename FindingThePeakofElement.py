'''
This question can besolved by binary search too, but it was little complicated, the solution below is
easy to understand and follow
'''

def peak(self,nums):
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            return i-1

    return len(nums)-1