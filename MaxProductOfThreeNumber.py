'''
We sort the array and take produc tof last three numbers of in case of negv numbers we take product of 
first two and last number
'''

def product3(self,nums):
    nums.sort()
    return max(nums[-1],nums[-2],nums[-3], num[0]*nums[1]*nums[-1])