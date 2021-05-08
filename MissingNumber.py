'''
initialize output array with -1's and then add the number of arrays
'''

def missing(self, nums):
    ret = [-1]*(len(nums)+1)

    for num in nums:
        ret[num] = num

    for i in range(len(nums)):
        if ret[i] == -1:
            return i