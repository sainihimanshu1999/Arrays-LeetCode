def findMedianSortedArrays(self,nums1,nums2):
    nums = nums1+nums2
    nums.sort()
    n = len(nums)

    if n%2==0:
        x = n//2
        y = x-1
        z = nums[x]+nums[y]
        return z/2.0
    else:
        x = n//2
        return nums[x]