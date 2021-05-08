'''
This is an easy question, it can be done using dictionary and set
'''

#dictionary

def duplicate(self,nums):
    dic = {}

    for num in nums:
        dic[num] = dic.get(num,0)+1

    for k,v in dic.items():
        if v>1:
            return True
    return False


#set

def duplicate(self,nums):
    return len(nums) != len(set(nums))