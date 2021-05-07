'''
In this question we have to find the longest consecutive subsequence of numbers from the given numbers.
'''

def LCS(self,nums):
    nums = set(nums)
    length = 0

    for x in nums:
        if x-1 not in nums:
            y = x+1
            while y in nums:
                y+=1

            length = max(length,y-x)

    return length