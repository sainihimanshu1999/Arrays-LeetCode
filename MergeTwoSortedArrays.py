'''
This is an easy question, just remember you can in place edit the array if you know the index and all
'''

def mergeTwoSortedArrays(self,nums1,m,nums2,n):
    if n == 0:
        return nums1

    for num in nums2:
        nums1[m] = num
        m+=1
    nums1.sort()