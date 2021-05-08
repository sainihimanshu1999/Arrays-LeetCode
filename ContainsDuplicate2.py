'''
In this question we hav to find the indices of two same number the get the abs(i-j) of them and 
then comapre it with a number given
'''

def duplicate(self,nums,k):
    dic = {}
    for i,num in enumerate(nums):
        if num in dic:
            if i -dic[num] <=k:
                return True

        dic[num] = i
    return False