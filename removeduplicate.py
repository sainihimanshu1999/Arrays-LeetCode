'''
Removal of duplicate inplace without changing the array
'''
def duplicate(self,nums):
    if not nums:
        return 0

    new = 0
    for i in range(1,len(nums)):
        if nums[i]!=nums[new]:
            new += 1
            nums[new] = nums[i]

    return new+1


'''
if new space formation is allowed
'''

nums[:] = sorted(set(nums))
return len(nums)