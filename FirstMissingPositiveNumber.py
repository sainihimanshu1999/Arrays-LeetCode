'''
This question requires very intutive approach, its'a hard question, but can be solved very easily.
Have a growth mindset
'''

def firstmissingpositive(self,nums):
    nums.sort()
    ans = 1
    for num in nums:
        if num ==  ans:
            ans+=1
    return ans