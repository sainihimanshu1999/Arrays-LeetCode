'''
setting all the zeroes to last of the arrays
'''

def moveZero(self,nums):
    for i in range(len(nums))[::-1]:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)

