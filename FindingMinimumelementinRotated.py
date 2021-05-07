'''
This question is same as part1 but it has duplicate elements, whenever we find duplicate element 
we decrease right by 1
'''

def findingtheminimumnumber(self,nums):
    left,right = 0,len(nums)-1

    while left<right:
        mid = (left+right)//2

        if nums[mid]>nums[right]:
            left = mid +1

        else:
            right = mid if nums[mid]!=nums[right] else right -1

    return nums[left]