'''
This question was easy we just have to find the length of longest increasing subsequence
'''

def LCI(seld,nums):
    count = 1
    maxi = 1

    for i in range(1,len(nums)):
        if nums[i-1]<nums[i]:
            count +=1
            maxi = max(maxi,count)

        else:
            count = 1

    return maxi