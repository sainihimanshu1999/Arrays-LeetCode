'''
In this question we hav to find the contigous subarray with maxproduct, we just take product forward 
and backwards then combine those array to get the maximum product out of them
'''

def maxProductsubarray(self,nums):
    a = nums[::-1]
    for i in range(1,len(nums)):
        nums[i] *= nums[i-1] or 1
        a[i] *= a[i-1] or 1

    return max(nums+a)