'''
In this question, we check if sum-k existed as previous sum at earlier stage, and keep expanding
the sum while checking whether we have seen (sum-k) before
'''

def subarray(self,nums,k):
    dic = {}
    dic[0] = 1
    s = 0 
    count = 0

    for i in range(len(nums)):
        s += nums[i]

        if s-k in dic:
            count += dic[s-k]

        if s in dic:
            dic[s] += 1

        else:
            dic[s] = 1
    return count