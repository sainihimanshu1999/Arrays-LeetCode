'''
use of counter in this question, and if k>0 we just have to find i+k in nums 
and if k==0 we just have to find the same number in nums
'''
from collections import Counter
def uniquePairs(self,nums,k):
    count = Counter(nums)
    if k>0:
        res = sum([i+k in count for i in count])

    else:
        res = sum([count[i]>1 for i in count])

    return res