'''
In rotated arrays we use binary search because, pivot can be on left or right side of the mid, when mid>right
pivot is on right side while if mid<=right it is on left side. Binary search should be our first approach
when tackling rotated arrays
'''

def findingtheminimumnumber(self,nums):
    left,right = 0, len(nums)-1

    while left<right:
        mid = (left+right)//2

        if nums[mid]>nums[right]:
            left = mid+1

        else:
            right = mid

    return nums[left]