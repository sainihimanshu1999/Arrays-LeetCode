'''
In this question we have use sliding window techinque, it is little difficult but very fast, two indices
pointer work simultaneously and result is updates after some condition
'''

def minimumSub(seld,nums,target):
    i,res = 0,len(nums)+1

    for j in range(len(nums)):
        target -= nums[j]
        while target<=0:
            res = min(res,j-i+1)
            target += nums[i]
            i +=1

    return res%(len(nums)+1)
