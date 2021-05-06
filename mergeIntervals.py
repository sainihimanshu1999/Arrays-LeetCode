'''
This question is easy to solve, ptr: 1. Whenever for loop is giving list index out of range, use while loop
2. del nums[i] faster than num.pop(i)
'''


def mergeIntervals(self,nums):
    nums = sorted(nums, key = lambda x:x[0])
    i = 0
    while i<=len(nums)-1:
        if nums[i][-1]>= nums[i+1][-1]:
            nums[i][-1] = max(nums[i][-1],nums[i+1][-1])
            del nums[i+1]
        else:
            i+=1
    return nums