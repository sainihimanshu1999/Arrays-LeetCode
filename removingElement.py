'''
In this question we only run the loop the times of value present in the array
'''

def removeElement(self,nums,val):
    for i in range(nums.count(val)):
        nums.remove(val)

    return len(nums)