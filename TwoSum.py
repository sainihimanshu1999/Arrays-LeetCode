'''
Leetcode two sum question, it is done using dictionary/hashmap and enumerate function, time complexity
is large
'''

def TwoSum(self,nums,target):
    dic = {}
    for index,value in enumerate(nums):
        remainder = target - value
        if remainder in dic:
            return[dic[remainder],index]
        else:
            dic[value] = index