'''
A triangle i said to be valid when the sum of any two sides is greated than third side
'''

def validTriangle(self,nums):
    count = 0
    nums.sort()
    n = len(nums)

    for i in range(n-1,1,-1):
        low = 0
        high = i-1

        while low<high:
            if nums[low]+nums[high]>nums[i]:
                count += low-high
                high -=1

            else:
                low +=1

    return count