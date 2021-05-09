'''
In this question we are maintaining an array of visited, once we come across visited we reset the step and
loop runs again
'''

def arrayNest(self,nums):
    res = 0
    count = 0
    seen = [False]*(len(nums))

    for i in range(len(nums)):
        while not seen[i]:
            seen[i] = True
            i = nums[i]
            count +=1

        res = max(res,count)
        count = 0

    return res