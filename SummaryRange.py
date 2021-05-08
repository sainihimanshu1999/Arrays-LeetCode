'''
This question is easy, we just have to check if there is any consecutive number is presend, if not
then we calculate the range 
'''

def summary(self,nums):
    if not nums:
        return []

    ans,i,start = [],0,0
    while i<len(nums)-1:
        if nums[i]+1 != nums[i+1]:
            ans.append(self.prange(nums[start],nums[i]))
            start = i+1

        i+=1
    ans.append(self.prange(nums[start],nums[i]))
    return ans



def prange(self,l,r):
    if l==r:
        return l
    else:
        return str(l) + '->'+ str(r)