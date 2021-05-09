'''
In this question sliding window technique is used
'''

def maxSub(self,nums,k):
    sumi = sum(nums[:k])
    maxi = sumi

    for i in range(1,len(nums)-k+1):
        sumi -= nums[i-1]
        sumi += nums[i+k-1]
        maxi = max(maxi,sumi)

    return float(maxi)/k
