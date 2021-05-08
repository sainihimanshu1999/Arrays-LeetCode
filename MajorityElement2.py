'''
This question can be solved using dictionary but to solve it in constant space we use boyer moore majority
vote algorithm, and in the algortithm we take two candidates instead of 1 and initialize it with 1, as
the solution will have less than or two answers
'''
#moore vote algo
def majority(self,nums):
    if not nums:
        return []

    count1,count2 = 0,0
    candidate1,candidate2 = 0,1

    for n in nums:
        if n ==  candidate1:
            count1 +=1

        elif n == candidate2:
            count2 +=1

        elif count1 == 0:
            candidate1 = n
            count1 =1

        elif count2 == 0:
            candidate2 = n
            count2 = 1

        else:
            count1 -=1
            count2 -=2

    return [n for n in (candidate1,candidate2) if nums.count(n)>len(nums)//3]


'''
Dictionary solution
'''

def majoritydic(self,nums):
    result = []
    dic= {}

    for num in nums:
        dic[num] =  dic.get(num,0)+1

    for k,v in dic.items():
        if v>len(nums)//2:
            result.append(k)

    return result